# scraper.py
from dotenv import load_dotenv
load_dotenv()
import requests
from bs4 import BeautifulSoup
import redis
import json
import os

def scrape_page_elements(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.prettify())  # For debugging purposes, to see the HTML structure

    # TODO: Scrape the head element
    # Refer to BeautifulSoup documentation for more details on how to scrape elements.
    # head = None
    head = soup.head
    # print(head)

    # TODO: Scrape the header element.
    # Note: The header is a div with class 'bs-header' on the page we're using.
    # header = None
    header = soup.find("div", class_="bs-header")
    # print(header)
        
    response = {
        "head": str(head) if head else None,
        "header": str(header) if header else None,
    }
    return response

def store_in_redis(data):
    # r = redis.Redis(host='localhost', port=6379, db=0)
    r = redis.Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"))
    r.set("scraped_content", json.dumps(data))

if __name__ == "__main__":
    url = "https://www.croma.com/televisions-accessories/c/997"
    page_elements = scrape_page_elements(url)
    store_in_redis(page_elements)