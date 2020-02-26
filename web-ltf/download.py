# 导包
import os

from selenium import webdriver
driver=webdriver.Chrome()
# 打开小说的目录页
driver.get('https://www.hongxiu.com/book/2810504401021002#Catalog')
# 定位所有的目录
url=driver.find_elements_by_css_selector('.volume .cf li a[href*="/"]')
# print(url)
http=[]
for i in url:
    # 获取所有目录中href的值添加到http中
    http.append(i.get_attribute("href"))
    # print(http)

def down(id):
    driver.get("https://www.hongxiu.com/book/"+id)

for id in http:
    down(id)
    # text=driver.find_element_by_css_selector('h3,p').text
    # if not os.mkdir('./story'):
    #     os.mkdir('./story')
    # newtext=open('./story/逃归.txt',mode='w',encoding='utf-8')
    # oldtxt=newtext.write(text)




