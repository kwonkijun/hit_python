import requests
from bs4 import BeautifulSoup

response = requests.get("https://startcoding-crawling.herokuapp.com/")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
sub_heading = soup.select_one(".subheading")
print(sub_heading.text)

