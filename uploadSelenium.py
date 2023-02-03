from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from time import sleep
import os
import demoji
from dotenv import load_dotenv
import logging
import random

logging.basicConfig(
    format="%(asctime)s -%(levelname)s  -  %(message)s ",
    encoding="utf-8",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    filename="log/anchor/system_anchor.log",
    filemode="a",
)


def upload_file(file_path, infos):
    os.system("clear")
    print(file_path)
    load_dotenv()
    url = "https://anchor.fm/dashboard/episode/new"
    email = os.getenv("EMAIL")
    passwd = os.getenv("PASSWORD")
    try:
        options = ChromeOptions()
        agentes = []
        with open("./user_Agents.txt") as file:
            for line in file:
                agentes.append(line)
        agente = agentes[random.randint(0, len(agentes) - 1)]
        options.add_argument(f"user-agent={agente}")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        print("iniciando upload")
        drive = Chrome(
            options=options, service=(Service(ChromeDriverManager().install()))
        )
        drive.get(url)
        print("preenchendo login")
        drive.find_element(by="id", value="email").send_keys(email)
        drive.find_element(by="id", value="password").send_keys(
            passwd, Keys.ENTER
        )
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
        ).send_keys(demoji.replace(infos["description"], ""))
        sleep(5)
        drive.find_element(
            By.XPATH, '//*[@id="app-content"]/div/form/div[1]/div[2]/button[2]'
        ).click()
        sleep(3)
        print("upload concluido com sucesso")
        logging.info("upload concluido com sucesso")
        drive.close()
    except (KeyboardInterrupt):
        logging.exception("upload interrompido")
        print("\nUpload interrompido")
    except Exception as e:
        logging.exception("esse é o erro ocorrido: %s", e)


if __name__ == "__main__":
    dist = {
        "title": "Falando com Maker mock",
        "description": "é um teste",
    }
    name = "./istockphoto-1316274253-640_adpp_is.mp3"
    upload_file(name, dist)
