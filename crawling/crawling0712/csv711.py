import requests
from bs4 import BeautifulSoup
import csv

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0"

fName = "test.csv"
f=open(fName,"w",encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title="N 종목명 현재가 전일비 등락률 액면가 시가총액 상장주식수 외국인비율 거래량 PER ROE"
title= title.split(" ")
writer.writerow(title)

res = requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,"html.parser")

myData = soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr") # 그냥 테이블 찾을때 첫번째에는 없어서 attrs 로 class 값의 type2를 찾음
for row in myData:
    columns = row.find_all("td")
    if len(columns) <= 1:
        continue
    data = [column.get_text().strip() for column in columns] # append 약식
    writer.writerow(data)
