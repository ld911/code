# 导模块
from appium import webdriver
from time import sleep
# 创建一个字典，包装相应的启动参数
desired_caps = dict()
# 需要连接的手机的平台(不限制大小写)
desired_caps['platformName'] = 'Android'
# 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
desired_caps['platformVersion'] = '5.1'
# 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
desired_caps['deviceName'] = 'huawei p30'
# 需要启动的程序的包名
desired_caps['appPackage'] = 'com.android.contacts'
# 需要启动的程序的界面名
desired_caps['appActivity'] = '.activities.PeopleActivity'

# 连接appium服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 定位通讯录上右下角的新建联系人图标并点击
driver.find_element_by_id('com.android.contacts:id/floating_action_button').click()
driver.find_element_by_id('com.android.contacts:id/left_button').click()
driver.find_element_by_xpath('//*[@package="com.android.contacts"]').send_keys("lv")
