import requests

response = requests.get("https://www.naver.com")
print(response.text) # HTML (문자열)