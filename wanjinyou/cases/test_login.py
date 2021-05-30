import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.page_login import LoginPage


@allure.feature("登录页面测试")
class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.page = LoginPage(self.driver)
        self.page.open_homepage()

    def teardown_method(self):
        self.driver.close()

    @pytest.mark.parametrize(
        "username,password,xpath",
        [
            pytest.param("13379190312", "Ld111111", "//*[text()=' 集团']",
                         id="测试正确登录"),

            pytest.param("133791903122", "Ld111111", "//*[text()='请输入正确的手机号！']",
                         id="测试登录失败-手机号错误"),

            pytest.param("13379190312", "111111", "//*[text()='密码错误']",
                         id="测试登录失败-密码错误"),

            pytest.param("", "", "//*[text()='请输入手机号或密码']",
                         id="测试登录失败-手机号密码都为空")
        ]
    )
    def test_login_check(self, username, password, xpath):
        """
        用指定用户名、密码登录，并检查xpath元素存在
        :param username: 用户名
        :param password: 密码
        :param xpath: 检查xpath元素
        """
        self.page.login(username, password)
        assert self.driver.find_element(By.XPATH, xpath)

    @allure.story("")
    def test_login_sms(self):
         self.page.input_username("13379190312")
         self.page.click_forget_password()
         self.page.send_phone_captcha()
         sleep(5)
         assert self.page.get_phone_captcha_button_text().startswith("重新发送")

