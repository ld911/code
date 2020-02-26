# Generated by Selenium IDE
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class TestTest():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_test(self):
        self.driver.get("https://www.hongxiu.com/book/12115534503935401")
        self.driver.set_window_size(1366, 768)
        self.driver.execute_script("window.scrollTo(0,100)")
        self.driver.find_element(By.ID, "j-closeGuide").click()
        self.driver.find_element(By.ID, "readBtn").click()
        self.driver.find_element(By.ID, "j-closeGuide").click()

        element = self.driver.find_element(By.CSS_SELECTOR, "#j_navCatalogBtn i")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#j_navCatalogBtn i").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "目录").click()
        self.vars["win2628"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win2628"])
        self.driver.find_element(By.ID, "readBtn").click()
