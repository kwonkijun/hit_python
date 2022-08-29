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

driver.implicitly_wait(15) # 페이지가 로딩될 때까지 최대 15초를 기다림
driver.get("https://startcoding-crawling.herokuapp.com/")
title = driver.find_element(By.CSS_SELECTOR, '.site-heading > h1')
print(title.text)

