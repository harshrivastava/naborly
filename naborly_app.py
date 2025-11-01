"""
Naborly — simple local social app prototype (Streamlit)
Region fixed to: Ward 12, ABC City

This is a single-file prototype using hardcoded dummy data.
Run: streamlit run naborly_app.py

Keep it beginner-friendly: edit the DATA structures below to change content.
"""

import streamlit as st
import pandas as pd
from datetime import datetime

# Page config
st.set_page_config(page_title="Naborly — Ward 12, ABC City", layout="wide")

# -----------------------------
# Dummy / static data (edit here)
# -----------------------------
REGION_NAME = "Ward 12, ABC City"

# Points for the map: shops, leaders, key points (latitude, longitude)
LOCATIONS = [
    {"name": "Green Grocers", "type": "Shop", "lat": 37.7749, "lon": -122.4194},
    {"name": "Asha Clinic", "type": "Service", "lat": 37.7756, "lon": -122.4183},
    {"name": "Community Hall", "type": "Key Point", "lat": 37.7768, "lon": -122.4170},
    {"name": "Local Leader - Mr. Roy", "type": "Leader", "lat": 37.7750, "lon": -122.4160},
    {"name": "Bakery Corner", "type": "Shop", "lat": 37.7740, "lon": -122.4205},
]

# Local news / bulletins
NEWS = [
    {"title": "Road repair on Main St", "date": "2025-11-01", "content": "Main St will have partial closures from Nov 3 to Nov 5 for resurfacing.", "tags": ["Transport", "Alert"]},
    {"title": "Health camp this weekend", "date": "2025-10-28", "content": "Free health checkup at Community Hall on Sunday 10am-2pm.", "tags": ["Health"]},
    {"title": "Festive cleanup drive", "date": "2025-10-20", "content": "Volunteer cleanup drive; meet at 8am near Bakery Corner.", "tags": ["Community"]},
]

# Directory of shops / services / leaders
DIRECTORY = [
    {"name": "Green Grocers", "type": "Shop", "contact": "+1-555-0101", "notes": "Groceries & vegetables"},
    {"name": "Asha Clinic", "type": "Service", "contact": "+1-555-0202", "notes": "General physician"},
    {"name": "Mr. Roy", "type": "Local Leader", "contact": "+1-555-0303", "notes": "Ward representative"},
]

# Community feed messages (dummy). This is read-only in files, but users can post during the session.
INITIAL_MESSAGES = [
    {"user": "Neha", "time": "2025-10-31 14:20", "message": "Does anyone know the pharmacy timings on Sundays?"},
    {"user": "Amit", "time": "2025-10-31 15:05", "message": "Garbage truck missed our lane today."},
    {"user": "Saira", "time": "2025-10-30 09:00", "message": "Looking for a tutor for grade 6 maths."},
]

# Utility schedules (fake)
UTILITIES = {
    "water_supply": [
        {"area": "North Block", "schedule": "Mon, Wed, Fri: 6am - 9am"},
        {"area": "South Block", "schedule": "Tue, Thu: 5pm - 8pm"},
    ],
    "garbage_collection": [
        {"area": "All Areas", "schedule": "Tue & Fri - 7am"},
    ],
}

# Notifications / alerts
NOTIFICATIONS = [
    {"level": "info", "text": "Novel community meeting on Nov 6 at 6pm, Community Hall."},
    {"level": "warning", "text": "Expect short water outage on Nov 3 morning due to maintenance."},
]

# -----------------------------
# Helper functions
# -----------------------------

def locations_to_dataframe(locations):
    """Convert list of location dicts to a pandas DataFrame for st.map"""
    df = pd.DataFrame(locations)
    # st.map expects latitude column 'lat' and longitude column 'lon'
    return df


def format_news_item(item):
    return f"**{item['title']}** — {item['date']}\n\n{item['content']}"

# -----------------------------
# UI Layout
# -----------------------------

# Top header and notifications
st.title(f"Naborly — {REGION_NAME}")

# Show notifications at top
with st.container():
    for note in NOTIFICATIONS:
        if note["level"] == "info":
            st.info(note["text"])
        elif note["level"] == "warning":
            st.warning(note["text"])
        elif note["level"] == "error":
            st.error(note["text"])

# Sidebar with quick info and filters
with st.sidebar:
    st.header("About this prototype")
    st.write("Fixed demo data for the region. No backend — static data only.")
    st.markdown("---")
    st.subheader("Region")
    st.write(REGION_NAME)
    st.markdown("---")
    st.subheader("Map filters")
    types = [loc["type"] for loc in LOCATIONS]
    types = sorted(list(set(types)))
    chosen = st.multiselect("Show types", options=types, default=types)

    st.markdown("---")
    st.subheader("Utilities quick view")
    for utype, entries in UTILITIES.items():
        st.write(f"**{utype.replace('_',' ').title()}**")
        for e in entries:
            st.write(f"- {e['area']}: {e['schedule']}")

# Main content: layout columns
col1, col2 = st.columns([2, 1])

# Left column: Map and Directory
with col1:
    st.subheader("Local Map")
    df_map = locations_to_dataframe([l for l in LOCATIONS if l["type"] in chosen])
    # st.map will show the geolocated points
    if not df_map.empty:
        st.map(df_map[["lat", "lon"]])
        st.write("**Points shown on the map:**")
        st.table(df_map[["name", "type"]])
    else:
        st.info("No locations to show. Adjust the filters in the sidebar.")

    st.markdown("---")
    st.subheader("Directory — Shops & Services")
    for entry in DIRECTORY:
        st.write(f"**{entry['name']}** ({entry['type']}) — {entry['contact']}\n\n_{entry['notes']}_")

# Right column: News, Feed, Utilities
with col2:
    st.subheader("Local News & Bulletins")
    for item in NEWS:
        st.markdown(format_news_item(item))
        st.markdown("---")

    st.subheader("Community Feed")
    # Initialize session messages (so users can post during the session)
    if 'messages' not in st.session_state:
        st.session_state['messages'] = INITIAL_MESSAGES.copy()

    with st.form(key='post_message'):
        user = st.text_input('Your name', value='You')
        msg = st.text_area('Post a message', placeholder='Share something with your neighbours...')
        submitted = st.form_submit_button('Post')
        if submitted and msg.strip():
            now = datetime.now().strftime('%Y-%m-%d %H:%M')
            st.session_state['messages'].insert(0, {"user": user, "time": now, "message": msg})

    # Display messages
    for m in st.session_state['messages'][:20]:
        st.write(f"**{m['user']}** — {m['time']}")
        st.write(m['message'])
        st.markdown("---")

    st.subheader("Utility Tracker")
    for utype, entries in UTILITIES.items():
        st.write(f"**{utype.replace('_',' ').title()}**")
        for e in entries:
            st.write(f"- {e['area']}: {e['schedule']}")

# Footer: quick tips for editing data
st.markdown("---")
st.caption("This is a static demo. To change content, edit the lists at the top of `naborly_app.py` (LOCATIONS, NEWS, DIRECTORY, INITIAL_MESSAGES, UTILITIES, NOTIFICATIONS).")

# Small helper: show raw data for debugging / learning
if st.checkbox('Show raw data (for learning)'):
    st.subheader('Raw DATA structures')
    st.write('LOCATIONS')
    st.write(LOCATIONS)
    st.write('NEWS')
    st.write(NEWS)
    st.write('DIRECTORY')
    st.write(DIRECTORY)
    st.write('UTILITIES')
    st.write(UTILITIES)
    st.write('NOTIFICATIONS')
    st.write(NOTIFICATIONS)

# Command to run the app
st.markdown("---")
st.code("python -m streamlit run naborly_app.py")
