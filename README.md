# Naborly — Local social app prototype

This is a small, beginner-friendly prototype of a local social app named "Naborly" for a fixed region (Ward 12, ABC City). It's built with Python and Streamlit and uses only hardcoded dummy data so you don't need a backend or database.

## What it includes

- Fixed map of the locality (dummy locations) using Streamlit's `st.map`.
- Local news, bulletins, and announcements (hardcoded sample data).
- Directory of shops, services, and local leaders with dummy contact info.
- Community feed/chat area with dummy messages (no backend; posts persist only during the Streamlit session).
- Utility tracker showing fake schedules for water supply and garbage pickup.
- Notifications and alerts shown inside the app.

## Tech stack

- Python 3.7+
- Streamlit
- pandas (for simple dataframes shown on the map)

## Files

- `naborly_app.py` — main Streamlit app (single-file prototype). Edit the DATA structures at the top to change dummy content.
- `requirements.txt` — Python packages required.

## Installation (Windows PowerShell)

1. Make sure Python 3.7+ is installed. You can check:

```powershell
python --version
```

If Python is not installed, download and install it from https://www.python.org/downloads/ (choose the latest 3.x). Make sure to check "Add Python to PATH" during installation.

2. (Optional) Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

3. Install required packages:

```powershell
python -m pip install -r requirements.txt
```

## Run the app

From the project folder (where `naborly_app.py` is), run:

```powershell
streamlit run naborly_app.py
```

This will open the app in your browser. The app is local and uses hardcoded sample data.

## How to modify the dummy data

Open `naborly_app.py` in a text editor. Near the top you will find clearly labeled lists/dictionaries:

- `LOCATIONS` — list of locations shown on the map. Each item is a dict with `name`, `type`, `lat`, `lon`.
- `NEWS` — list of news items, each with `title`, `date`, `content`, `tags`.
- `DIRECTORY` — list of shops/services/leaders with `name`, `type`, `contact`, `notes`.
- `INITIAL_MESSAGES` — messages shown in the community feed when the app starts.
- `UTILITIES` — fake schedules for water, garbage collection.
- `NOTIFICATIONS` — alerts shown at the top of the app.

Edit or add items to those lists, save, and refresh the Streamlit app page to see changes.

## Notes and next steps

- This is a static prototype for demonstration. To make it real, you would add a backend (database + API), authentication, persistent chat, and real map tiles.
- Small recommended improvements: add icons on the map (pydeck/folium), search/filtering in the directory, and simple tests to validate data formats.

Enjoy exploring the prototype and customizing the dummy data!
