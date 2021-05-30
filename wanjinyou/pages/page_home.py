from poium import Element
from poium import CSSElement

from base.base_page import BasePage


class HomePage(BasePage):
    """
    首页
    """

    menu_item_company_management = Element(xpath="//*[text()='企业管理']")
    menu_item_my_companies_list = Element(xpath="//*[text()='我的企业列表']")
    menu_item_company_settlement = Element(xpath="//*[text()='企业结算']")
