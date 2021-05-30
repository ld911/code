# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDefaultSuite():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test1(self):
    # Test name: test1
    # Step # | name | target | value
    # 1 | open | /Login.html | 
    self.driver.get("http://tvip.nucarf.cn/Login.html")
    # 2 | setWindowSize | 1374x776 | 
    self.driver.set_window_size(1374, 776)
    # 3 | click | id=username | 
    self.driver.find_element(By.ID, "username").click()
    # 4 | type | id=username | 13589812345
    self.driver.find_element(By.ID, "username").send_keys("13589812345")
    # 5 | click | name=password | 
    self.driver.find_element(By.NAME, "password").click()
    # 6 | type | name=password | 123456789
    self.driver.find_element(By.NAME, "password").send_keys("123456789")
    # 7 | click | id=login_button | 
    self.driver.find_element(By.ID, "login_button").click()
    # 8 | mouseOver | id=login_button | 
    element = self.driver.find_element(By.ID, "login_button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 9 | mouseOut | id=login_button | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 10 | click | css=.rememberme > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".rememberme > span").click()
    # 11 | click | id=login_button | 
    self.driver.find_element(By.ID, "login_button").click()
    # 12 | assertNotChecked | css=.rememberme | 
    assert self.driver.find_element(By.CSS_SELECTOR, ".rememberme").is_selected() is False