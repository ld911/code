from poium import Element
from poium import CSSElement

from base.base_page import BasePage


class MyCompaniesList(BasePage):
    """
    我的企业列表
    """
    # 按钮
    Inquire_button = Element(xpath="//*[text()='查询']")
    modify_button = Element(xpath="//*[text()='修改']")
    more_button = Element(xpath="//*[text()=' 更多']")
    company_configuration_button = Element(xpath="//*[text()='企业配置']")
    account_details_button = Element(xpath="//*/a[text()='账户详情']")
    account_details_close_button = Element(class_name="btn dark btn-outline")
    account_management_button = Element(xpath="//*/a[text()='账户管理']")
    stored_value_record_button = Element(xpath="//*/a[text()='储值记录']")
    company_transfer_record_button = Element(xpath="//*/a[text()='企业转账记录']")
    # 文本
    company_list_text = Element(xpath="//*[text()='企业列表']")
    account_type_text = Element(xpath="//*[text()='账户类型']")
