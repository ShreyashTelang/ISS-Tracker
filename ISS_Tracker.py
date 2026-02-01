import requests
import json
import webbrowser
import folium

# json API endpoint to get the current location of the ISS
url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url).json()

# Extract latitude and longitude of the ISS
latitude = float(response['iss_position']['latitude'])
longitude = float(response['iss_position']['longitude'])

# Display the ISS location
print(f"Tracking ISS: Latitude: {latitude}, Longitude: {longitude}")

# Creat a folium map centered on the ISS location
map = folium.Map(location = [latitude, longitude], zoom_start = 4)
folium.Marker([latitude, longitude], popup="International Space Station").add_to(map)
map.save("ISS_Location.html")

# Open the location in Google Maps
google_map_url = f"https://www.google.com/maps?q={latitude},{longitude}"
webbrowser.open(google_map_url)