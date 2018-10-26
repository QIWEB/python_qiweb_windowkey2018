# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()

browser.get("D:\python_dome\outlook\Product Keys - My Visual Studio.htm")
#import time
#time.sleepl
'''
Windows 10 Pro 101
Windows 10 Pro N and KN  =101 -46 =55
'''
ysh =browser.find_elements(By.TAG_NAME,"span")
print "span size：",len(ysh)
ysh=browser.find_elements_by_class_name("claim-key-link")
print "a size：",len(ysh)
xx=browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr[700]/td[1]/span")
#ysh =browser.find_element(By.TAG_NAME,"span"))
#for span in ysh:
from selenium.webdriver.common.keys import Keys
for span in ysh:
    num =ysh.index(span) + 1
    txt=span.get_attribute("aria-label")
    print num,txt
    if 'for Windows 10 Pro N and KN' in txt:
        #span.click()
        span.send_keys(Keys.ENTER)  # 键盘输入enter
        print u'已经点击'
    #if span.get_attribute("aria-label") in 9: #获取标 签属性
    #if span.text=='Windows 10 Education N and KN':

    #    print span
#browser.close()

#给用户名的输入框标红

js="var q=document.getElementById(\"user_name\");q.style.border=\"1px solid red\";"
js='''$('a[aria-label="索取密钥 for Office 2007 Applications"]')[5].click();$('#downloadSearchBox').val("9999")'''
#调用js

browser.execute_script(js)
print browser.get_cookies()

