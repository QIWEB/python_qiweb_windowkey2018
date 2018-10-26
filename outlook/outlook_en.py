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
        driver.get(
            "https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1528799945&rver=6.7.6640.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3df55afda9-347d-ebc9-2a89-6b30da60ff18&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&uaid=e8e7e1d8b25a4cfbbb8c9fc2b2eb1767&lic=1")
        driver.find_element_by_id("MemberName").click()
        driver.find_element_by_id("MemberName").clear()
        driver.find_element_by_id("MemberName").send_keys("ujmrfvber0009")
        driver.find_element_by_id("iSignupAction").click()
        driver.find_element_by_id("PasswordInput").click()
        driver.find_element_by_id("PasswordInput").clear()
        driver.find_element_by_id("PasswordInput").send_keys("yuikm89-,")
        driver.find_element_by_id("iSignupAction").click()
        driver.find_element_by_id("FirstName").click()
        driver.find_element_by_id("FirstName").clear()
        driver.find_element_by_id("FirstName").send_keys("poiux")
        driver.find_element_by_id("LastName").click()
        driver.find_element_by_id("LastName").clear()
        driver.find_element_by_id("LastName").send_keys("wxfil")
        driver.find_element_by_id("iSignupAction").click()
        driver.find_element_by_id("Country").click()
        Select(driver.find_element_by_id("Country")).select_by_visible_text("Cameroon")
        driver.find_element_by_id("Country").click()
        driver.find_element_by_id("BirthMonth").click()
        Select(driver.find_element_by_id("BirthMonth")).select_by_visible_text("July")
        driver.find_element_by_id("BirthMonth").click()
        driver.find_element_by_id("BirthDay").click()
        Select(driver.find_element_by_id("BirthDay")).select_by_visible_text("15")
        driver.find_element_by_id("BirthDay").click()
        driver.find_element_by_id("BirthYear").click()
        Select(driver.find_element_by_id("BirthYear")).select_by_visible_text("2006")
        driver.find_element_by_id("BirthYear").click()
        driver.find_element_by_id("iSignupAction").click()
        driver.find_element_by_id("iSignupAction").click()
        driver.find_element_by_id("wlspispSolutionElement1f562dab0ea74b76ae8adfbef48ed4ad").click()
        driver.find_element_by_id("wlspispSolutionElement1f562dab0ea74b76ae8adfbef48ed4ad").clear()
        driver.find_element_by_id("wlspispSolutionElement1f562dab0ea74b76ae8adfbef48ed4ad").send_keys("6w6k3")
        driver.find_element_by_id("iSignupAction").click()
        driver.find_element_by_xpath("//button/i").click()
        driver.find_element_by_xpath("//div/div/div/div").click()
        driver.find_element_by_id("rw_3__listbox__option__118").click()
        driver.find_element_by_xpath("//div[2]/div/div/div").click()
        driver.find_element_by_id("rw_4__listbox__option__98").click()
        driver.find_element_by_xpath("//button[2]/i").click()
        driver.find_element_by_xpath(
            "//img[contains(@src,'https://r4.res.office365.com/owa/prem/16.2375.5.2569166/resources/themes/chevron//images/0/themepreview.png')]").click()
        driver.find_element_by_xpath("//button[2]/i").click()
        driver.find_element_by_xpath("//button[2]/i").click()
        driver.find_element_by_xpath("//button").click()
        driver.find_element_by_xpath("//div[@id='lgnDiv']/div[8]/div/span").click()
        driver.find_element_by_id("selTz").click()
        Select(driver.find_element_by_id("selTz")).select_by_visible_text(
            u"‎(UTC-07:00)‎ Mountain Time ‎(US & Canada)‎")
        driver.find_element_by_id("selTz").click()
        driver.find_element_by_xpath("//div[@id='lgnDiv']/div[8]/div/span").click()
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/div/div/div[3]/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/span").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
