import requests
import json

# Replace YOUR_API_KEY with your actual API key
api_key = "AIzaSyBfbd6ScZnfRfZSm-HBjg78gF5SEq7G2m8"

# Replace CHANNEL_ID with the ID of the channel you want to check
channel_id = "UCidmlliiEyQjaiKGZ69F3GQ"

# Make a GET request to the YouTube Data API
url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}"
response = requests.get(url)

# Convert the response to a JSON object
data = json.loads(response.text)

# Get the subscriber count from the JSON object
subscriber_count = data["items"][0]["statistics"]["subscriberCount"]

# Print the subscriber count
print(f"This channel has {subscriber_count} subscribers.")








