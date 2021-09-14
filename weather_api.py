import requests
from bs4 import BeautifulSoup

def getTemp():
    uri = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8"

    response = requests.get(uri)
    soup = BeautifulSoup(response.text, "html.parser")
    target = soup.select_one("#main_pack .sc_new .main_info .todaytemp")
    temperature = target.string
    temp = {"temp" : temperature}

    print(type(temp))

    return temp
