
# -*- coding: utf-8 -*-
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time
#分模块测试，txt写入测试
#driver_item=webdriver.Firefox()
driver_item=webdriver.PhantomJS(executable_path="phantomjs.exe")
url="https://movie.douban.com/subject/3541415/?tag=%E7%A7%91%E5%B9%BB&from=gaia_video"
wait = ui.WebDriverWait(driver_item,10)
driver_item.get(url)

try:
    driver_item.find_element_by_xpath("//img[@class='bn-arrow']").click()
    #wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='review-bd']/div[2]/div/div"))
    time.sleep(1)
    comments_deep = driver_item.find_element_by_xpath("//div[@class='review-bd']/div[2]/div")

    print u"深度长评："+comments_deep.text
    #print type(comments_deep.text)#<type 'unicode'>

    comments_wr=comments_deep.text.encode('utf-8')
    #print type(comments_wr)#<type 'str'>

    #title="盗梦空间"#中文命名文件名乱码，内容可用
    title="Inception"
    with open("%s.txt"%title,"w") as f:#格式化字符串还能这么用！
        for i in comments_wr:
            f.write(i)
except:
    print 'can not caught the comments!'