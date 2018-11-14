#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

# 用 w 設定模式創立編碼
f = open(os.getcwd()+ "/data.txt",'w',encoding="utf8")

driver = webdriver.Chrome(os.getcwd() + "/chromedriver",chrome_options=options)



for i in range(1819,1821):
    driver.get("https://www.ptt.cc/bbs/NBA_Film/index" + str(i) + ".html")
    sourcecode = BeautifulSoup(driver.page_source,"html.parser")
    #print(sourcecode)
    sections = sourcecode.find_all("div","r-ent")
    for section in sections:
        sourcecode2 = BeautifulSoup(str(section),"html.parser")
        titles = sourcecode2.find_all("div","title")[0].text
        if titles.find("公告") == -1:
            print(titles)
            push = sourcecode2.find_all("div","nrec")[0].text
            print(push)
            author = sourcecode2.find_all("div","author")[0].text
            print(author)
            date = sourcecode2.find_all("div","date")[0].text
            print(date)
            data = titles + "\n" + push + "\n" + author + "\n" + date
            f.write(data)

driver.quit()


f.close()


# In[13]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(os.getcwd() + "/chromedriver",chrome_options=options)

import pymysql.cursors
connection = pymysql.connect(host="localhost",
                            user="root",password="mpyhacct012",db="technews",
                            charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)

for i in range(1819,1821):
    driver.get("https://www.ptt.cc/bbs/NBA_Film/index" + str(i) + ".html")
    sourcecode = BeautifulSoup(driver.page_source,"html.parser")
    #print(sourcecode)
    sections = sourcecode.find_all("div","r-ent")
    for section in sections:
        sourcecode2 = BeautifulSoup(str(section),"html.parser")
        title = sourcecode2.find_all("div","title")[0].text
        if title.find("公告") == -1:
            print(title)
            push = sourcecode2.find_all("div","nrec")[0].text
            print(push)
            author = sourcecode2.find_all("div","author")[0].text
            print(author)
            date = sourcecode2.find_all("div","date")[0].text
            print(date)
            with connection.cursor() as cursor:
                sql = '''INSERT INTO `technews`.`ptt_crawler`(title,push,author,date)
                VALUES(%s,%s,%s,%s);'''.format("title","push","author","date")
                val = (title,push,author,date)
                cursor.execute(sql,val)
                connection.commit()
                result=cursor.fetchall()


driver.quit()
connection.close()


# In[ ]:




