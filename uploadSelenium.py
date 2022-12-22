from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

from dotenv import load_dotenv


def upload_file(file_path):
    load_dotenv()
    url = "https://anchor.fm/login"
    email = os.getenv("EMAIL")
    passwd = os.getenv("PASSWORD")
    drive = Firefox()
    drive.get(url)
    drive.find_element(by="id", value="email").send_keys(email)
    drive.find_element(by="id", value="password").send_keys(passwd, Keys.ENTER)

    sleep(10)
    drive.close()
    

if __name__ == "__main__":
    upload_file("path/to/file")
