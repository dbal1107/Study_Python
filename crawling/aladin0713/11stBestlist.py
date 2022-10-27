import requests
from bs4 import BeautifulSoup

url = "https://books.11st.co.kr/booksmall/BooksAction.tmall?ID=BOOKS&ctgrNo=63548&srCtgrNo=63518"

res = requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,"html.parser")
bookData = soup.select(".product_conts")

for book in bookData:
    bookRank = book.select(".flg_ranking")[0].get_text()
    bookName = book.select(".pub_photo")[0].find("img")["alt"]
    bookAuthor = book.select(".book_info")[0].find_all("a")[0].get_text()
    if "! " in bookName:
        bookName = bookName.split("! ")[1]
    else:
        bookName = bookName
    if "상품상세설명 참조" in bookAuthor:
        bookAuthor = bookAuthor.replace("상품상세설명 참조","NONE")
    elif "확인중" in bookAuthor:
        bookAuthor = bookAuthor.replace("확인중","NONE")
    else:
        bookAuthor = bookAuthor
    print(f'''{bookRank}) {bookName}
    {bookAuthor}''')
    print("-"*80)
