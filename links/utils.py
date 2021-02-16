import requests
import lxml
from bs4 import BeautifulSoup
import unicodedata


def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()
    try:
        price = soup.select_one(selector="#priceblock_dealprice").getText(strip=True)
    except Exception as e:
        #print('No Deal Price Available')
        price = soup.select_one(selector="#priceblock_ourprice").getText(strip=True)
        

    price = unicodedata.normalize("NFKD", price[1:])
    price = price.replace(',','')
    price = float(price)
    return name, price
