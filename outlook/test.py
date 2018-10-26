# -* - coding: UTF-8 -* -
import urllib2
import cookielib
#获取Cookiejar对象（存在本机的cookie消息）
cookie = cookielib.CookieJar()
#自定义opener,并将opener跟CookieJar对象绑定
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#安装opener,此后调用urlopen()时都会使用安装过的opener对象
urllib2.install_opener(opener)
request = urllib2.Request("https://outlook.live.com/owa/")
request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0')
response = urllib2.urlopen(request)
print response.getcode()
print response.geturl()
print response.read()

print '=============================================================='
print '=============================================================='
print '=============================================================='
request = urllib2.Request("https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1528788087&rver=6.7.6640.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3d9b34e37c-0fb4-eb0c-1e3a-53f8879abaef&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&uaid=ff47a3f3c1674b779aacef1c61554b8f&lic=1")
request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0')
response = urllib2.urlopen(request)
print response.getcode()
print response.geturl()
#Set-Cookie: ClientId=3BC01204C2E54B78B2402F486D9BA34E; expires=Wed, 12-Jun-2019 03:22:45 GMT; path=/; secure
#Set-Cookie: ClientId=3BC01204C2E54B78B2402F486D9BA34E; expires=Wed, 12-Jun-2019 03:22:45 GMT; path=/; secure
#Set-Cookie: HostSwitchPrg=; expires=Sun, 12-Jun-1988 03:22:45 GMT; path=/; secure
#Set-Cookie: OptInPrg=; expires=Sun, 12-Jun-1988 03:22:45 GMT; path=/; secure
#Set-Cookie: logonLatency=LGN01=636643705651269706; domain=live.com; path=/; secure; HttpOnly
#Set-Cookie: O365Consumer=; expires=Sun, 12-Jun-1988 03:22:45 GMT; path=/; secure

print response.read()