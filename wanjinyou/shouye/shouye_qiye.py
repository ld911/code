from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
class Shouye_qiye(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get()
        self.driver.add_cookie({"name": "PHPSESSID", "value": "8cg4peeob6pgmd50ugag0nqh48"})
        self.driver.add_cookie({"name": "", "value": ""})
    def tearDown(self) -> None:
        pass
    #测试首页企业管理
    def test_case6(self):
        self.driver.find_element(BY.XPATH, "//*[text()='企业管理']").click()

    #测试首页企业管理下我的企业列表
    def test_case7(self):
        self.driver.find_element(BY.XPATH, "//*[text()='我的企业列表']").click()

    # 测试首页企业管理下企业结算
    def test_case8(self):
        self.driver.find_element(BY.XPATH, "//*[text()='企业结算']").click()




