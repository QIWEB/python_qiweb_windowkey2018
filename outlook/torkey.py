# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://my.visualstudio.com/productkeys")
        driver.find_element_by_xpath("//form[@id='i0281']/div/div").click()
        driver.find_element_by_id("i0116").click()
        driver.find_element_by_id("i0116").clear()
        driver.find_element_by_id("i0116").send_keys("roastinomlm@outlook.com")
        driver.find_element_by_id("idSIButton9").click()
        driver.find_element_by_id("i0118").click()
        driver.find_element_by_id("i0118").clear()
        driver.find_element_by_id("i0118").send_keys("61nG55hAvs2q")
        driver.find_element_by_id("idSIButton9").click()
        driver.find_element_by_id("idSIButton9").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='我们还需要一些详细信息'])[1]/following::form[1]").click()
        driver.find_element_by_id("create-profile-submit-btn").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Windows 10 Pro'])[13]/following::a[1]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
