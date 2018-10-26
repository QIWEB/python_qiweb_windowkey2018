# coding=utf-8
from selenium import webdriver
import time,json
import pprint
# 等待视频播放
time.sleep(5)
# 获得所有网络请求
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=test")
js='''$("#su").submit()'''
#调用js

driver.execute_script(js)
performance_data = driver.execute_script("return window.performance.getEntries();")
pprint.pprint(performance_data)

print 111111111111111111111
print driver.get_cookies()
print 111111111111111111111

print driver.log_types
for entry in driver.get_log('driver'):
    print entry
lo = driver.get_log('driver')
# 聚合 请求分类
datalist = {}
for entry in lo:

    try:
        m = json.loads(entry['message'])['message']["params"]["response"]
        k = m['headers']['Content-Type']
        url = m['url']
        if k not in datalist:
            datalist[k] = [url]
        else:
            datalist[k].append(url)

            # print( "-------------------------")
    except Exception as e:
        continue
# 页面存在的 播放过的视频
videolist = []
filename = ""
for x in datalist:
    if x.find("video") > -1:
        filename = x.replace("video/", ".")
        videolist = datalist[x]

# 保存视频 在当前目录
for x in range(0, len(videolist)):
    pass
    #urllib.request.urlretrieve(videolist[x], str(x) + filename)
