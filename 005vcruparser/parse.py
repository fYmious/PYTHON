import requests
from bs4 import BeautifulSoup

url = "https://vc.ru/popular"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for article in soup.find_all("div", class_="content content--short"):
    title = article.div.div.text.strip()
    link = article.a['href']

    print(title, link)
