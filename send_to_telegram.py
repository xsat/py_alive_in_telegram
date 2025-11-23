from dotenv import load_dotenv
from os import getenv
from datetime import datetime
from requests import post
from time import sleep


def py_alive_in_telegram() -> None:
    load_dotenv()

    url: str = f"https://api.telegram.org/bot{getenv("TOKEN")}/sendMessage"
    chat_id: str | None = getenv("CHAT_ID")
    check_time_in_seconds: int = 60

    while(True):
        post(url, data={"chat_id": chat_id, "text": datetime.now()})
        sleep(check_time_in_seconds)


if __name__ == "__main__":
    py_alive_in_telegram()
