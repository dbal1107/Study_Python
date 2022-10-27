from bs4 import BeautifulSoup
from selenium import webdriver

import pymysql.cursors


url = "https://www.starbucks.co.kr/menu/drink_list.do"

dr = webdriver.Chrome("./chromedriver")
dr.get(url)

title = "메뉴, 칼로리, 당류, 단백질, 나트륨, 포화지방, 카페인 정보"
title = title.split(", ")


soup = BeautifulSoup(dr.page_source,"html.parser")

data = soup.find_all("table",attrs={"class":"coffeeInfo mb60"})




connection = pymysql.connect(host='localhost',
                             port=3307,
                             user='root',
                             password='7777',
                             database='baemin',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:

    with connection.cursor() as cursor:
        sql = "INSERT INTO `drink` ( `menu`, `kcal`, `sugar`, `protein`, `fat`, `caffeine` ) VALUES ( %s, %s, %s, %s, %s, %s )"
        for info in data:
            detail = info.select("tbody")
            for kcal in detail:
                drink = kcal.select("tr")
                for x in drink:
                    d = [y.get_text() for y in x.select("td")]
                    cursor.execute(sql, (d[0],d[1],d[2],d[3],d[4],d[5]))
    connection.commit()


    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `drink` WHERE `sugar` > 20"
        cursor.execute(sql)
        result = cursor.fetchall()
        for re in result:
            print(re)

dr.quit()