import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv
import re
from index import main
load_dotenv()
url = f"https://www.googleapis.com/youtube/v3/search?key={os.getenv('API_KEY')}&channelId={os.getenv('CHANNEL_ID')}&part=snippet,id&order=date&maxResults=1"
response = requests.get(url)
data = json.loads(response.text)
time = datetime.strptime(
    data["items"][0]["snippet"]["publishedAt"], "%Y-%m-%dT%H:%M:%SZ"
)
if time.date() == datetime.now().date():
    title = data["items"][0]["snippet"]["title"]
    if re.search(r"estr", title, re.IGNORECASE):
        last_video_url = f"https://www.youtube.com/watch?v={data['items'][0]['id']['videoId']}"
        main(last_video_url)
else:
    print("No video today")
