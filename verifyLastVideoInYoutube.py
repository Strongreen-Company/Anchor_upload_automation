import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv
import re
import logging
from index import main
from EmailClass import email_sender


logging.basicConfig(
    format="%(asctime)s -%(levelname)s  -  %(message)s ",
    encoding="utf-8",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    filename="/var/log/anchor/system_anchor.log",
    filemode="w",
)
load_dotenv()


def verify_video():

    try:
        url = f"""https://www.googleapis.com/youtube/v3/search?key={os.getenv('API_KEY_YOUTUBE')}&channelId={os.getenv('CHANNEL_ID')}&part=snippet,id&order=date&maxResults=1"""
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
            email_sender().send_sucesso()
            logging.info("episodio postado hoje com sucesso")
        else:
            email_sender().send_falha()
            logging.error("o video não foi postado hoje")
    except Exception as e:
        logging.exception("esse é o erro ocorrido: %s", e)


if __name__ == "__main__":
    verify_video()
