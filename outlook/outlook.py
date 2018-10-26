#! /usr/bin/env python
#coding=utf-8

import urllib2
import urllib
import cookielib

def login():
    email = raw_input("请输入用户名:")
    pwd = raw_input("请输入密码:")
    data={

    }  #登陆用户名和密码
    post_data=urllib.urlencode(data)   #将post消息化成可以让服务器编码的方式
    cj=cookielib.CookieJar()   #获取cookiejar实例
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    #自己设置User-Agent（可用于伪造获取，防止某些网站防ip注入）
    headers ={
        'Host': 'outlook.live.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        #'Cookie': 'ClientId=6298D8C36F7B4C8F8EBD3CB33973BECA; MSFPC=GUID=e01333eca0e54186b8afe20a2968de2a&HASH=e013&LV=201806&V=4&LU=1528770975656; optimizelyEndUserId=oeu1528770974815r0.17131261796514408; OWAPF=p:00000111&v:16.2375.5.2569166&l:mouse&',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    website = raw_input('请输入网址:')
    website='https://outlook.live.com/owa/'
    req=urllib2.Request(website,headers)
    content=opener.open(req)
    print content.read()    #linux下没有gbk编码，只有utf-8编码

if __name__ == '__main__':
    login()