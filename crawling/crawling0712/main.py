import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from requests import *

# driver = webdriver.Chrome("/Users/admin/Desktop/crowling/chromedriver")
url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

# print(len(res.text))

# with open("webtoon.html", "w", encoding="utf8") as f:
#     f.write(res.text)

soup=BeautifulSoup(res.text,"html.parser")
# print(soup.title.get_text())
# print(soup.ol)
# print(soup.ol.attrs)
# myList = soup.ol
# print(myList.a)
# print(myList.a.get_text())
#--------------------------------------
# myList= soup.ol.select("a") # a가 들어있는 모든걸 뽑기
#
# for x in myList:
#     rank = x["onclick"].split(",")
#     print(f"Rank {rank[3][1:-2]} : {x.get_text()}")
# -------------------------------------------------
myList= soup.ol.select("li")
# print(myList)
for x in myList:
    print(x["class"][0], x.select("a")[0].get_text())

    # 핵심 기준 찾아내기 -> 너무 많은 갯수: 상위 폴더 찾기 ->