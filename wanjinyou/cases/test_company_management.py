import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.page_login import LoginPage
from pages.page_home import HomePage
from pages.page_companies_list import MyCompaniesList

@allure.feature("企业管理测试")
class TestCompanyManagement:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        login_page = LoginPage(self.driver)
        login_page.open_homepage()
        login_page.login("13379190312", "Ld111111")
        self.home_page = HomePage(self.driver)
        self.company_page = MyCompaniesList(self.driver)

    def setup_method(self):
        if not self.home_page.menu_item_my_companies_list.is_displayed():
            self.home_page.menu_item_company_management.click()

        self.home_page.menu_item_my_companies_list.click()

    def teardown_class(self):
        self.driver.close()


    @allure.story("点击修改")
    def test_click_modify(self):
        self.company_page.modify_button.click()

    @allure.story("点击更多")
    def test_click_more(self):
        self.company_page.more_button.click()

    @allure.story("点击更多下的企业配置")
    def test_click_company_configuration(self):
        self.company_page.more_button.click()
        self.company_page.company_configuration_button.click()

    @allure.story("点击更多下的账户详情")
    def test_click_account_details(self):
        self.company_page.more_button.click()
        self.company_page.account_details_button.click()
        self.driver.refresh()


    @allure.story("点击更多下的账户管理")
    def test_click_account_management(self):
        self.company_page.more_button.click()
        self.company_page.account_management_button.click()
        assert self.company_page.account_management_button

    @allure.story("点击更多下的储值记录")
    def test_click_stored_value_record(self):
        self.company_page.more_button.click()
        self.company_page.stored_value_record_button.click()

    @allure.story("点击更多下的企业转账记录")
    def test_click_company_transfer_record(self):
        self.company_page.more_button.click()
        self.company_page.company_transfer_record_button.click()

    @allure.story("打开企业结算")
    def test_open_company_settlement(self):
        self.home_page.menu_item_company_settlement.click()



















    # @pytest.mark.parametrize(
    #     "item,check_element",
    #     [
    #         pytest.param(self.company_page.company_configuration_button,
    #                      None,
    #                      id="点击更多下的企业配置"),
    #
    #         pytest.param(self.company_page.account_details_button,
    #                      self.company_page.account_type_text,
    #                      id="点击更多下的账户详情"),
    #
    #         pytest.param(self.company_page.account_management_button,
    #                      self.company_page.account_type_text,
    #                      id="点击更多下的账户管理"),
    #     ]
    # )
    # def test_click_items_under_more(self, item, check_element):
    #     """
    #     测试点击"更多"下面的每一个菜单项
    #     :return:
    #     """
    #     self.company_page.more_button.click()
    #     item.click()
    #     if check_element is not None:
    #         assert check_element


