import requests
from bs4 import BeautifulSoup as bs

def url_to_soup(url):
    """
    Helper function, returns relevant BeautifulSoup object for investments, divestments and portfolio URL.
    :param url: url to EQT investments, divestments or portfolio site
    :return: soup object filtered on relevant elements
    """
    scraped = requests.get(url, verify=False)
    funds_soup_raw = bs(scraped.content, "html.parser")
    return funds_soup_raw.find_all("li", class_="flex flex-col border-t border-neutral-light cursor-pointer sm:cursor-default")
