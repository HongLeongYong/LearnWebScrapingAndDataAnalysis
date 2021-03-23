import requests
from bs4 import BeautifulSoup

resp = requests.get("http://blog.castman.net/py-scraping-analysis-book/ch1/connect.html")
soup = BeautifulSoup(resp.text, "html.parser")
print(soup.find("h1").text)