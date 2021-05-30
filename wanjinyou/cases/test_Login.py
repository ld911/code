from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.page_login import LoginPage


class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.page = LoginPage(self.driver)
        self.page.open_homepage()

    def teardown_method(self):
        self.driver.close()

    def login_check(self, username, password, xpath):
        """
        用指定用户名、密码登录，并检查xpath元素存在
        :param username:
        :param password:
        :param xpath:
        :return:
        """
        self.page.input_username(username)
        self.page.input_password(password)
        self.page.click_login()
        assert self.driver.find_element(By.XPATH, xpath)

    # case1测试正确登录
    def test_case1(self):
        self.login_check("13379190312", "Ld111111", "//*[text()=' 集团']")

    # 测试登录失败-手机号错误
    def test_case2(self):
        self.login_check("133791903122", "Ld111111", "//*[text()='请输入正确的手机号！']")

     # 测试登录失败-密码错误
    def test_case3(self):
        self.login_check("13379190312", "111111", "//*[text()='密码错误']")

    # 测试登录失败-手机号密码都为空
    def test_case4(self):
        self.login_check("", "", "//*[text()='请输入手机号或密码']")

    # 测试发送验证码
    def test_case5(self):
        self.page.input_username("13379190312")
        self.page.click_forget_password()
        self.page.send_phone_captcha()
        sleep(5)
        assert self.page.get_phone_captcha_button_text().startswith("重新发送")

    # # 退出登录
    # def test_case6(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://tvip.nucarf.cn/Login.html")
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element(By.ID, "username").click()
    #     self.driver.find_element(By.ID, "username").send_keys("13379190312")
    #     self.driver.find_element(By.NAME, "password").click()
    #     self.driver.find_element(By.NAME, "password").send_keys("Ld111111")
    #     self.driver.find_element(By.ID, "login_button").click()
    #     self.driver.implicitly_wait(10)
    #     self.driver.set_window_size(1261, 760)
    #     self.driver.find_element(By.LINK_TEXT, "退出登录").click()