import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.amazon.in/s?k=dell&page='+str(page)+'+2&qid=1559802912&ref=sr_pg_2'
        source_code = requests.get(url)
        plain_text = source_code.text.encode("utf-8")
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.find_all('a', {'class': 'a-link-normal a-text-normal'}):
            href = 'https://www.amazon.in'+link.get('href')
            print(href)
            with open("Directory.txt", "a", encoding="utf-8") as f:
                    f.write(str(href)+"\n")
            get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item_name in soup.findAll('span', {'id': 'productTitle'}):
        print(item_name.string)
        with open("Directory.txt", "a", encoding="utf-8") as f:
            f.write(str(item_name.string) + "\n")
    for price in soup.findAll('span', {'id': 'priceblock_ourprice'}):
        with open("Directory.txt", "a", encoding="utf-8") as f:
            f.write(str(price.string) + "\n")
        print(price.string)


trade_spider(10)
