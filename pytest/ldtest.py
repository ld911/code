# 导包
from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.action_chains import ActionChains

## 提交测试


# 实例化浏览器
driver=webdriver.Chrome()
# 打开红袖网
# driver.get('https://www.hongxiu.com/')
driver.get('https://www.hongxiu.com/book/12115534503935401#Catalog')
# 设置隐士等待
driver.implicitly_wait(10)
# # 定位弹出页面
# driver.find_element_by_id('j-guidePopup')
# # 定位关闭符号，并点击
# driver.find_element_by_id('j-closeGuide').click()
# # 定位登录图标并点击
# driver.find_element_by_id('j-avatar').click()
# # 切换页面
# driver.switch_to.frame('loginIfr')
# # 定位用户名输入框并输入
# driver.find_element_by_xpath('//*[@id="username"]').send_keys('13379190312')
# driver.find_element_by_xpath('//*[@id="password"]').send_keys('13379190312ld')
# driver.find_element_by_link_text('登 录').click()
# driver.maximize_window()
# # 定位免费元素
# driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div[1]/ul/li[3]/a').click()
# driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/a[2]').click()
# # 对要打开的书进行元素定位
# driver.find_element_by_xpath('//*[text()="含羞"]').click()
# 定位所有的[data-rid]属性
data_rid=driver.find_elements_by_css_selector('[data-rid]')

b=[]
# b 这个列表里是data-rid的值
for i in data_rid:
    shu=i.get_attribute('data-rid')
    b.append(int(shu))

bb=list(set(b))
# 将列表去重并排序
for ii in bb:
    a=str(ii)
    # 循环点击a 标签
    driver.find_element_by_xpath('// li[ @ data - rid = '+a +']/a').click()
#     这个循环里面我想实现循环定位点击并读取文本并写入
quit()


