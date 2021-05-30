from poium import Element

from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    登录页面
    """
    # # 控件定位方式
    # css = "xx"
    # id_ = "xx"
    # name = "xx"
    # xpath = "xx"
    # link_text = "xx"
    # partial_link_text = "xx"
    # tag = "xx"
    # class_name = "xx"
    username = Element(name="username", describe="用户名输入框")
    password = Element(name="password", describe="密码输入框")
    login_button = Element(id_="login_button", describe="登录按钮")
    forget_password = Element(id_="forget-password2", describe="忘记密码链接")
    get_phone_captcha = Element(id_="getPhoneCaptcha", describe="获取验证码按钮")

    def login(self, username, password):
        """
        用指定用户名、密码登录
        :param username:
        :param password:
        """
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_button.click()
