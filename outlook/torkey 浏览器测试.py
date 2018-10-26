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
        #设置10秒

        #driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);

        #设置国家和地区第一次登录会用到
        #driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='我们还需要一些详细信息'])[1]/following::form[1]").click()
        #driver.find_element_by_id("create-profile-submit-btn").click()
        #刷新
        driver.get("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=&tn=baidu&bar=&wd=ip&rn=&oq=&rsv_pq=c17336a700002dfb&rsv_t=697dFbJrjE1SKUz%2BbD0OJlozccnDqAemToSBSdgTB13lOm0EqpSoxP6vEqw&rqlang=cn")



        #time.sleep(5)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Windows 10 Pro'])[13]/following::a[1]").click()

        time.sleep(500)

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
