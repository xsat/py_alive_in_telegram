from logging import getLogger, Logger, basicConfig, INFO
from dotenv import load_dotenv
from os import getenv
from datetime import datetime
from requests import post, Response
from time import sleep


def py_alive_in_telegram() -> None:
    logger: Logger = getLogger("py_alive_in_telegram")
    
    basicConfig(level=INFO)
    
    try:
        logger.info("Try to load dotenv")
        load_dotenv()

        url: str = f"https://api.telegram.org/bot{getenv("TOKEN")}/sendMessage"
        chat_id: str | None = getenv("CHAT_ID")
        check_time_in_seconds: int = 60
        
        logger.info("Staring loop")
        while(True):
            text: str = datetime.now().isoformat()
            logger.info(f"Make request to telegram, text: {text}")
            response: Response = post(url, data={"chat_id": chat_id, "text": text})
            if not response.ok:
                logger.warning(f"Not ok response: {response}")
            
            logger.info(f"Going to sleep for {check_time_in_seconds} seconds")
            sleep(check_time_in_seconds)
            
    except Exception as exception:
        logger.exception(exception)


if __name__ == "__main__":
    py_alive_in_telegram()
