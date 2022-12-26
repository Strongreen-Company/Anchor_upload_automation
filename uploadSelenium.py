from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

from dotenv import load_dotenv


def upload_file(file_path, infos):
    os.system("clear")
    print(file_path)
    load_dotenv()
    url = "https://anchor.fm/dashboard/episode/new"
    email = os.getenv("EMAIL")
    passwd = os.getenv("PASSWORD")
    try:
        options = ChromeOptions()
        # options.add_argument("--headless")
        print("iniciando upload")
        drive = Chrome(options=options)
        drive.get(url)
        print("preenchendo login")
        drive.find_element(by="id", value="email").send_keys(email)
        drive.find_element(by="id", value="password").send_keys(passwd, Keys.ENTER)
        sleep(5)
        print("preenchendo arquivo")
        inputFile = drive.find_element(By.TAG_NAME, "input")
        drive.execute_script("arguments[0].style.display='block';", inputFile)
        inputFile.send_keys(os.path.abspath(file_path))
        print("aguardando upload")
        wait = WebDriverWait(drive, 500)
        element = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/div/div/main/div/div/div/div/div[2]/button",
                )
            )
        ).click()
        print("Upload concluído", element)
        sleep(5)
        print("preenchendo informações")
        drive.find_element(By.ID, "title").send_keys(infos["title"])
        drive.find_element(
            By.XPATH,
            '//*[@id="app-content"]/div/form/div[4]/div[2]/div[2]/div/div/div[2]/div/div[2]/div',
        ).send_keys(infos["description"])
        sleep(5)
        drive.find_element(By.XPATH, "//*[@id=\"app-content\"]/div/form/div[1]/div[2]/button[2]").click()
        sleep(3)
        print("Episódio publicado")
        drive.close()
    except (KeyboardInterrupt):
        print("\nUpload interrompido")

if __name__ == "__main__":
    dist = {
        "title": "Falando com Maker Comece cedo mas saiba onde quer chegar! [Thais Sadami]",
        "description": "é um teste"
    }
    name = "./audio/Falando com Maker De qual lado da força você está Definindo prioridades e fazendo escolhas[Divina].mp3"
    upload_file(name, dist)
