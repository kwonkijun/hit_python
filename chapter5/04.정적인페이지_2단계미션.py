import requests
from bs4 import BeautifulSoup

for i in range(1, 5):
    print(f"====={i}페이지 입니다.=====")
    response = requests.get(f"https://startcoding-crawling.herokuapp.com/lv1?page={i}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.select('.post-preview')

    for post in posts:
        title = post.select_one('.post-title')
        subtitle = post.select_one('.post-subtitle')
        link = post.select_one(".post-meta > a")

        print("=====제목=====")
        print(title.text + "\n")
        
        print("=====설명=====")
        print(subtitle.text + "\n")
        
        print("=====링크=====")
        print(link.attrs['href'] + "\n")


        