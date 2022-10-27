from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = "https://www.youtube.com/results?search_query="
data = input("뭘볼거야? : ")

sUrl = baseUrl + data

print(sUrl)

dr = webdriver.Chrome("/Users/admin/Desktop/crowling/chromedriver")
dr.get(sUrl)

hd=dr.page_source
bs_txt = BeautifulSoup(hd, "html.parser")

mydata = bs_txt.select("#video-title")
# print(mydata)
for x in mydata:
    print(x.get("title"))
    y=x.get("href")
    if y != None:
        print(y.split("=")[1])

dr.close()