from bs4 import BeautifulSoup
from selenium import webdriver
import csv

url = "https://www.starbucks.co.kr/menu/drink_list.do"

dr = webdriver.Chrome("D:\chromeDriver\chromedriver.exe")
dr.get(url)

fName = "starbugs.csv"
f = open(fName, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "메뉴, 칼로리, 당류, 단백질, 나트륨, 포화지방, 카페인 정보"
title = title.split(", ")
writer.writerow(title)

soup = BeautifulSoup(dr.page_source,"html.parser")

data = soup.find_all("table",attrs={"class":"coffeeInfo mb60"})
# print(data)
# print(data.select("caption"))

for info in data:
    detail = info.select("tbody")
    for kcal in detail:
        drink = kcal.select("tr")
        for x in drink:
            d = [y.get_text() for y in x.select("td")]
            writer.writerow(d)

dr.close()