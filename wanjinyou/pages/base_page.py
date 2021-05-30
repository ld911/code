from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from poium import Page, Element

class BasePage(Page):

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
