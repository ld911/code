

# 打开设置并点击右上角放大镜功能，点击搜索框输入10086

# 导模块
from appium import webdriver
from time import sleep
import time
from selenium.webdriver.support.wait import WebDriverWait
# 创建一个字典，包装相应的启动参数
desired_caps = dict()
# 需要连接的手机的平台(不限制大小写)
desired_caps['platformName'] = 'Android'
# 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
desired_caps['platformVersion'] = '5.1'
# 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
desired_caps['deviceName'] = '192.168.56.101:5555'
# 需要启动的程序的包名
desired_caps['appPackage'] = 'com.android.settings'
# 需要启动的程序的界面名
desired_caps['appActivity'] = '.Settings'

desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 连接appium服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# # 定位设置中的放大镜元素，并点击
# driver.find_element_by_id('com.android.settings:id/search').click()
# # 定位搜索框，并输入10086
# driver.find_element_by_id('com.android.settings:id/search').send_keys("10086")
# sleep(3)
# # 清空
# driver.find_element_by_id('com.android.settings:id/search').clear()
# sleep(2)
# # 输入123
# driver.find_element_by_id('com.android.settings:id/search').send_keys("123")
# driver.find_element_by_xpath('//*[@content-desc="收起"]').click()
# 跳转到通讯录页面     driver.start_activity（包名，界面名）
# driver.start_activity('com.android.contacts','.activities.PeopleActivity')
# 获取包名和界面名
# print(driver.current_package)
# print(driver.current_activity)
# # 如果存在tpshop这个软件就卸载，否则就安装
# if driver.is_app_installed('com.tpshop.malls'):
# # 卸载tpshop
#     driver.remove_app('com.tpshop.malls')
# else:
#     driver.install_app('D:\就业班\qijiAPP\通用\com.tpshop.malls_2.1.0.apk')

# 关闭当前的程序
# driver.close_app()
# 关闭驱动
# driver.quit()
# 显示等待
# WebDriverWait(driver,10,1).until(lambda driver:driver.find_element_by_id('com.android.settings:id/title'))
# time.sleep(10)




