import requests
from bs4 import BeautifulSoup

response = requests.get("https://startcoding-crawling.herokuapp.com/lv2")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.select('.post-preview')
print(posts)

