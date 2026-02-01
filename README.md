# ISS-Tracker
Fetches live geographic coordinates of ISS from the Open Notify API.

ISS Real-Time Tracker 🛰️
A lightweight Python script that fetches the current location of the International Space Station (ISS) using the Open Notify API and visualizes it on both an interactive Leaflet map and Google Maps.

🚀 Features
Real-time Data: Fetches live geographic coordinates from the Open Notify API.

Interactive HTML Map: Generates a local .html file using folium with a marker placed at the ISS's current position.

Instant Browser View: Automatically opens your default web browser to the location on Google Maps.

📂 File Structure
iss_tracker.py: The main Python script.

ISS_Location.html: The interactive map generated after execution.

💻 How It Works
API Request: The script sends a GET request to http://api.open-notify.org/iss-now.json.

Data Parsing: It extracts the latitude and longitude from the JSON response.

Map Generation: * Folium: Creates a zoomable map saved as ISS_Location.html.

Webbrowser: Launches a Google Maps URL using the coordinates.

Note: The Google Maps URL format used in the script is: https://www.google.com/maps?q=latitude,longitude
