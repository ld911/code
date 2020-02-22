# # 导模块
# from appium import webdriver
# # 创建一个字典、包装相应的启动参数
# desired_caps=dict()
# # 需要连接手机的平台
# desired_caps['platfromName']='andriod'
# # 需要连接手机的版本号
# desired_caps['platfromVersion']='8.1.0'
# # 需要连接手机的设备号
# desired_caps['deviceName']='YH5PIVUWW4CMT4BU'
# # 需要启动的程序的包名
# desired_caps['devicePackage']='com.leyuz.bbs.leyuapp'
# # 需要启动程序的界面名
# desired_caps['AppActivity']='.DaohangActivity'
#
# # 连接appium服务器
# driver=webdriver.WebElement('http://localhost:4723/wd/hub', desired_caps)



# 导模块
from appium import webdriver
# 创建一个字典、包装相应的启动参数
desired_caps=dict()
# 需要连接手机的平台
desired_caps['platfromName']='andriod'
# 需要连接手机的版本号
desired_caps['platfromVersion']='5.1'
# 需要连接手机的设备号
desired_caps['deviceName']='YH5PIVUWW4CMT4BU'
# 需要启动的程序的包名
desired_caps['devicePackage']='com.leyuz.bbs.leyuapp'
# 需要启动程序的界面名
desired_caps['AppActivity']='.DaohangActivity'

# 连接appium服务器
driver=webdriver.WebElement('http://localhost:4723/wd/hub', desired_caps)