import requests
from bs4 import BeautifulSoup
import os


class Scraper:
    @staticmethod
    def price_fetch(url1):
        url = url1
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/83.0.4103.61 Safari/537.36"}

        page = requests.get(url=url, headers=header)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(id="productTitle").get_text()
        t = soup.find(id="pd").get
        price = soup.find(id="priceblock_ourprice").get_text()
        # print("Amazon:", title.strip())
        # print("Price:", amazon_price)
        with open('price.txt', 'a', encoding="utf-8") as file:
            file.write("Title:" + title.strip())
            file.write("\nPrice:" + price.strip())
            file.close()
        os.startfile('price.txt')


if __name__ == '__main__':
    Scraper.price_fetch(
        "https://www.amazon.in/AMD-Ryzen-3600X-Processor-100000022BOX/dp/B07SQBFN2D/ref=sr_1_3?crid=1YMMGC3P5UCCC"
        "&dchild=1&keywords=3600x&qid=1591191234&sprefix=3600%2Caps%2C292&sr=8-3")
