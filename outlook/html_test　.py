# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
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
    #临时添加就是不想只想这个for
    continue
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
js='''$('a[aria-label="索取密钥 for Office 2007 Applications"]')[5].click();function test(){$('#downloadSearchBox').val("9999"); } $('#downloadSearchBox').val("77777"); setTimeout('test()', 5000);  var aa=%s; return aa;'''%[12,34,56,7]
#调用js

print browser.execute_script(js)
import time


arr1 = []
# js脚本模板
jstemp1 = '''
    //正则表达式 后面g表示匹配多行 返回数组
    var pattern = /[A-Z0-9]{5}-{1}[A-Z0-9]{5}-{1}[A-Z0-9]{5}-{1}[A-Z0-9]{5}-{1}[A-Z0-9]{5}/g;
    //这个数组是没有发送请求之前网页源代码中的所有html和文本
    var str=$("body").text();
    var attr1=str.match(pattern);
    return attr1;
    '''
jstemp2 = '''
    //用jquery 模拟 点击一个连接后请求服务器，返回了一个激活码串 展示在界面上
    //$('a[aria-label="索取密钥 for Office 2007 Applications"]')[5].click();
    //$("#qiwebdiv").html("发送请求后服务器返回了这个内容：C64GF-QGX43-2PMM3-KFGKM-Q6600");
    //在每个 div 元素结尾插入内容
    $("div").append(" <b>Hello world!发送请求后服务器返回了这个内容：C64GF-QGX43-2PMM3-KFGKM-Q6600</b>")
 '''
jstemp3 = '''
    //去除数组重复元素
    function uniqueqiweb(arr){
      var hash=[];
      for (var i = 0; i < arr.length; i++) {
        for (var j = i+1; j < arr.length; j++) {
          if(arr[i]===arr[j]){
            ++i;
          }
        }
          hash.push(arr[i]);
      }
      return hash;
    }
    //正则表达式 后面g表示匹配多行 返回数组
    var pattern = /[A-Z0-9]{5}-{1}[A-Z0-9]{5}-{1}[A-Z0-9]{5}-{1}[A-Z0-9]{5}-{1}[A-Z0-9]{5}/g;
    //再获取一遍网页上的全部内容，用正则提取我们需要的激活码
    var str=$("body").text();
    var arr2=str.match(pattern);
    var str1="%s";//python传进来的数组字符串 a，b，c 
    arr1 = str1.split(",");// 在每个逗号(,)处进行分解  ["abc", "abcd", "aaa"]
    //这个数组是从更新后的数组中比较之前页面上的信息，返回页面请求后新增的内容数组
    arr3=arr2.filter(key => !arr1.includes(key))

    //但是arr3 包含重复的元素 这里再去重处理

    var arr5=uniqueqiweb(arr3);
    //这个内容返回给python 
    return arr5;
''' #% arr1  # [12,34,5]这个数组后续改成脚本1的返回值

#1、获取最原始的页面结果数组
arr1= browser.execute_script(jstemp1)
print  arr1

#python 数组转字符串
#arr=[u'C64GF-QGX43-2PMM3-KFGKM-Q66PR', u'HVCBT-WQ823-BHMJC-RQJ3P-9T9VT', u'KHCYK-2DXWD-6D4BV-9D9K6-TT9RY']
str1 = ','.join(arr1)
#C64GF-QGX43-2PMM3-KFGKM-Q66PR,HVCBT-WQ823-BHMJC-RQJ3P-9T9VT,KHCYK-2DXWD-6D4BV-9D9K6-TT9RY
print str1
#js字符串转数组
#var s = "abc,abcd,aaa";
#ss = s.split(",");// 在每个逗号(,)处进行分解  ["abc", "abcd", "aaa"]


#2、模拟点击 获取最新key
browser.execute_script(jstemp2)
#3、等待数据加载
time.sleep(5)
jstemp3=jstemp3%str1
print jstemp3
#4、比较加载后数据获取最新的key
arr5= browser.execute_script(jstemp3)

print arr5