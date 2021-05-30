from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    """
    页面基础类，承载公共属性和方法
    """

    def __init__(self, driver):
        """
        构造方法
        :param driver: Selenium Driver
        """
        self.driver = driver

    def wait_visibility(self, locator):
        """
        等待元素显示出来
        :param locator:
        :return:
        """
        WebDriverWait(self.driver, 222).until(expected_conditions.visibility_of_element_located(locator))

    def wait_presence(self, locator):
        """
        等待元素在DOM加载出来（不一定是显示出来可见的状态）
        :param locator:
        :return:
        """
        WebDriverWait(self.driver, 222).until(expected_conditions.presence_of_element_located(locator))

    def open_homepage(self):
        """
        打开网站首页
        :return:
        """
        self.driver.get("http://tvip.nucarf.cn/Login.html")
        self.driver.implicitly_wait(10)
