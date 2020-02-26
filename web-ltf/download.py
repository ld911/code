# 导包
import os
from time import sleep

from selenium import webdriver
driver=webdriver.Chrome()
# 打开小说的目录页
driver.get('https://www.hongxiu.com/book/2810504401021002#Catalog')
# 定位所有的目录
url=driver.find_elements_by_css_selector('.volume .cf li a[href*="/chapter/"]')
urls=[]
for i in url:
    # 获取所有目录中href的值添加到urls中
    urls.append(i.get_attribute("href"))
for id in urls:
    driver.get(id)
    text=driver.find_elements_by_css_selector('h3,p')
    for txt in text:
        book=txt.text
        with open('./story/逃归.txt','a',encoding='utf-8') as t:
            t.write(book)






