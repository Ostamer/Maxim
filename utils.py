import os
from dotenv import load_dotenv
import requests
from loguru import logger

# Загружаем переменные окружения из .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
LOG_FILE = os.getenv("LOG_FILE")

logger.add(LOG_FILE)


def get_artwork_by_id(object_id: int):
    url = f"{BASE_URL}/objects/{object_id}"
    logger.info(f"GET {url}")
    response = requests.get(url)
    logger.info(f"Response {response.status_code}: {response.text}")
    return response


def search_artworks_with_query(query: str):
    url = f"{BASE_URL}/search?q={query}"
    logger.info(f"GET {url}")
    response = requests.get(url)
    logger.info(f"Response {response.status_code}: {response.text}")
    return response
