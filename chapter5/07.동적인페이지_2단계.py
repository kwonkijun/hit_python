from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

sv = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=sv, options=chrome_options)
driver.implicitly_wait(5) 
# [selenium 기본 설정 코드 붙여넣기]
from selenium.webdriver.common.keys import Keys
import time

driver.get("https://startcoding-crawling.herokuapp.com/lv2")
time.sleep(2)

# 스크롤 전 데이터 개수 확인
posts = driver.find_elements(By.CSS_SELECTOR, '.post-preview') 
before_count = len(posts)

while True:
    # 스크롤 내리기
    body = driver.find_element(By.CSS_SELECTOR, 'body')
    body.send_keys(Keys.END)

    # 스크롤 사이 로딩 시간
    time.sleep(2)

    # 스크롤 후 로딩된 데이터 개수 확인
    posts = driver.find_elements(By.CSS_SELECTOR, '.post-preview') 
    after_count = len(posts)

    # 스크롤 전, 후 개수 같다면 반복 멈춤
    if before_count == after_count:
        break

    # 스크롤 전 개수를 업데이트
    before_count = after_count

for post in posts:
    title = post.find_element(By.CSS_SELECTOR, '.post-title')
    subtitle = post.find_element(By.CSS_SELECTOR, '.post-subtitle')
    link = post.find_element(By.CSS_SELECTOR, ".post-meta > a")

    print("=====제목=====")
    print(title.text + "\n")
    
    print("=====설명=====")
    print(subtitle.text + "\n")
    
    print("=====링크=====")
    print(link.get_attribute('href') + "\n")


    