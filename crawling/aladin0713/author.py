import requests
from bs4 import BeautifulSoup

url = "https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1"

res = requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,"html.parser")

bookData = soup.select(".ss_book_box")
# s = bookData[0].find_all("li")

for idx, i in enumerate(bookData):
    s = bookData[idx].find_all("li")
    author = s[2].get_text().split("|")[0]
    print(author)

# print(bookData)
# for i in authorData:
#     print(i.get(""))

# for x in mydata:
#     print(x.get("title"))
#     y=x.get("href")
#     if y != None:
#         print(y.split("=")[1]) # none 이 생기면 안나와서 if로 따로 골라줌
#
# dr.close()