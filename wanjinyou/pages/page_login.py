from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    登录页面
    """

    def input_username(self, username):
        """
        输入用户名

        :param username: 用户名
        :return:
        """
        self.wait_visibility((By.ID, "username"))
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys(username)

    def input_password(self, password):
        """
        输入密码

        :param password: 密码
        :return:
        """
        self.wait_visibility((By.NAME, "password"))
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys(password)

    def click_login(self):
        """
        点击登录按钮
        :return:
        """
        self.wait_visibility((By.ID, "login_button"))
        self.driver.find_element(By.ID, "login_button").click()

    def click_forget_password(self):
        """
        点击发送短信验证
        :return:
        """
        self.driver.find_element(By.ID, "forget-password2").click()

    def send_phone_captcha(self):
        """
        发送短信验证
        :return:
        """
        self.driver.find_element(By.ID, "getPhoneCaptcha").click()

    def get_phone_captcha_button_text(self):
        """
        获取“发送短信验证按钮”上显示的文字
        :return:
        """
        return self.driver.find_element(By.ID, "getPhoneCaptcha").text
