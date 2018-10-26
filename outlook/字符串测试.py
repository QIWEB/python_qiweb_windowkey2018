#python 数组转字符串
arr=[u'C64GF-QGX43-2PMM3-KFGKM-Q66PR', u'HVCBT-WQ823-BHMJC-RQJ3P-9T9VT', u'KHCYK-2DXWD-6D4BV-9D9K6-TT9RY']
str1 = ','.join(arr)
#C64GF-QGX43-2PMM3-KFGKM-Q66PR,HVCBT-WQ823-BHMJC-RQJ3P-9T9VT,KHCYK-2DXWD-6D4BV-9D9K6-TT9RY
print str1
#js字符串转数组
#var s = "abc,abcd,aaa";
#ss = s.split(",");// 在每个逗号(,)处进行分解  ["abc", "abcd", "aaa"]

arr2 = str1.split(',')
print arr2