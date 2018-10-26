# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import random
import json


class UntitledTestCase(unittest.TestCase):
    country_list=[
        "AL",
        "DZ",
        "AF",
        "AR",
        "AE",
        "AW",
        "OM",
        "AZ",
        "AC",
        "EG",
        "ET",
        "IE",
        "EE",
        "AD",
        "AO",
        "AI",
        "AG",
        "AT",
        "AX",
        "AU",
        "MO",
        "BB",
        "PG",
        "BS",
        "PK",
        "PY",
        "PS",
        "BH",
        "PA",
        "BR",
        "BY",
        "BM",
        "BG",
        "MP",
        "BJ",
        "BE",
        "IS",
        "PR",
        "PL",
        "BA",
        "BO",
        "BZ",
        "BW",
        "BQ",
        "BT",
        "BF",
        "BI",
        "BV",
        "KP",
        "GQ",
        "DK",
        "DE",
        "TL",
        "TP",
        "TG",
        "DO",
        "DM",
        "RU",
        "EC",
        "ER",
        "FR",
        "FO",
        "PF",
        "GF",
        "TF",
        "MF",
        "VA",
        "PH",
        "FJ",
        "FI",
        "CV",
        "FK",
        "GM",
        "CG",
        "CD",
        "CO",
        "CR",
        "GG",
        "GD",
        "GL",
        "GE",
        "CU",
        "GP",
        "GU",
        "GY",
        "KZ",
        "HT",
        "KR",
        "NL",
        "AN",
        "HM",
        "ME",
        "HN",
        "KI",
        "DJ",
        "KG",
        "GN",
        "GW",
        "CA",
        "GH",
        "GA",
        "KH",
        "CZ",
        "ZW",
        "CM",
        "QA",
        "KY",
        "CC",
        "KM",
        "XK",
        "CI",
        "KW",
        "HR",
        "KE",
        "CK",
        "CW",
        "LV",
        "LS",
        "LA",
        "LB",
        "LT",
        "LR",
        "LY",
        "LI",
        "RE",
        "LU",
        "RW",
        "RO",
        "MG",
        "IM",
        "MV",
        "MT",
        "MW",
        "MY",
        "ML",
        "MH",
        "MQ",
        "YT",
        "MU",
        "MR",
        "US",
        "AS",
        "UM",
        "VI",
        "MN",
        "MS",
        "BD",
        "PE",
        "FM",
        "MM",
        "MD",
        "MA",
        "MC",
        "MZ",
        "MX",
        "NA",
        "ZA",
        "AQ",
        "GS",
        "SS",
        "NR",
        "NP",
        "NI",
        "NE",
        "NG",
        "NU",
        "NO",
        "NF",
        "PW",
        "PN",
        "PT",
        "MK",
        "JP",
        "SE",
        "CH",
        "SV",
        "WS",
        "RS",
        "YU",
        "SL",
        "SN",
        "CY",
        "SC",
        "XS",
        "SA",
        "BL",
        "CX",
        "ST",
        "SH",
        "KN",
        "LC",
        "SX",
        "SM",
        "PM",
        "VC",
        "XE",
        "LK",
        "SK",
        "SI",
        "SJ",
        "SZ",
        "SD",
        "SR",
        "SB",
        "SO",
        "TJ",
        "TW",
        "TH",
        "TZ",
        "TO",
        "TC",
        "TA",
        "TT",
        "TN",
        "TV",
        "TR",
        "TM",
        "TK",
        "WF",
        "VU",
        "GT",
        "VE",
        "BN",
        "UG",
        "UA",
        "UY",
        "UZ",
        "ES",
        "GR",
        "HK",
        "SG",
        "NC",
        "NZ",
        "HU",
        "SY",
        "JM",
        "AM",
        "XJ",
        "YE",
        "IQ",
        "IR",
        "IL",
        "IT",
        "IN",
        "ID",
        "UK",
        "VG",
        "IO",
        "JO",
        "VN",
        "ZM",
        "JE",
        "TD",
        "GI",
        "CL",
        "CF",
        "CN"

    ]
    country_map={
        "AL": "阿尔巴尼亚",
        "DZ": "阿尔及利亚",
        "AF": "阿富汗",
        "AR": "阿根廷",
        "AE": "阿拉伯联合酋长国",
        "AW": "阿鲁巴",
        "OM": "阿曼",
        "AZ": "阿塞拜疆",
        "AC": "阿森松岛",
        "EG": "埃及",
        "ET": "埃塞俄比亚",
        "IE": "爱尔兰",
        "EE": "爱沙尼亚",
        "AD": "安道尔",
        "AO": "安哥拉",
        "AI": "安圭拉岛",
        "AG": "安提瓜和巴布达",
        "AT": "奥地利",
        "AX": "奥兰岛",
        "AU": "澳大利亚",
        "MO": "澳门特别行政区",
        "BB": "巴巴多斯",
        "PG": "巴布亚新几内亚",
        "BS": "巴哈马",
        "PK": "巴基斯坦",
        "PY": "巴拉圭",
        "PS": "巴勒斯坦民族权力机构",
        "BH": "巴林",
        "PA": "巴拿马",
        "BR": "巴西",
        "BY": "白俄罗斯",
        "BM": "百慕大群岛",
        "BG": "保加利亚",
        "MP": "北马里亚纳群岛",
        "BJ": "贝宁",
        "BE": "比利时",
        "IS": "冰岛",
        "PR": "波多黎各",
        "PL": "波兰",
        "BA": "波斯尼亚和黑塞哥维那",
        "BO": "玻利维亚",
        "BZ": "伯利兹",
        "BW": "博茨瓦纳",
        "BQ": "博内尔",
        "BT": "不丹",
        "BF": "布基纳法索",
        "BI": "布隆迪",
        "BV": "布维岛",
        "KP": "朝鲜",
        "GQ": "赤道几内亚",
        "DK": "丹麦",
        "DE": "德国",
        "TL": "东帝汶",
        "TP": "东帝汶",
        "TG": "多哥",
        "DO": "多米尼加共和国",
        "DM": "多米尼克",
        "RU": "俄罗斯",
        "EC": "厄瓜多尔",
        "ER": "厄立特里亚",
        "FR": "法国",
        "FO": "法罗群岛",
        "PF": "法属波利尼西亚",
        "GF": "法属圭亚那",
        "TF": "法属南部领地",
        "MF": "法属圣马丁",
        "VA": "梵蒂冈",
        "PH": "菲律宾",
        "FJ": "斐济",
        "FI": "芬兰",
        "CV": "佛得角",
        "FK": "福克兰群岛",
        "GM": "冈比亚",
        "CG": "刚果（布）",
        "CD": "刚果（金）",
        "CO": "哥伦比亚",
        "CR": "哥斯达黎加",
        "GG": "格恩西岛",
        "GD": "格林纳达",
        "GL": "格陵兰",
        "GE": "格鲁吉亚",
        "CU": "古巴",
        "GP": "瓜德罗普岛",
        "GU": "关岛",
        "GY": "圭亚那",
        "KZ": "哈萨克斯坦",
        "HT": "海地",
        "KR": "韩国",
        "NL": "荷兰",
        "AN": "荷属安的列斯(前)",
        "HM": "赫德和麦克唐纳群岛",
        "ME": "黑山",
        "HN": "洪都拉斯",
        "KI": "基里巴斯",
        "DJ": "吉布提",
        "KG": "吉尔吉斯斯坦",
        "GN": "几内亚",
        "GW": "几内亚比绍",
        "CA": "加拿大",
        "GH": "加纳",
        "GA": "加蓬",
        "KH": "柬埔寨",
        "CZ": "捷克",
        "ZW": "津巴布韦",
        "CM": "喀麦隆",
        "QA": "卡塔尔",
        "KY": "开曼群岛",
        "CC": "科科斯群岛(基灵群岛)",
        "KM": "科摩罗联盟",
        "XK": "科索沃",
        "CI": "科特迪瓦",
        "KW": "科威特",
        "HR": "克罗地亚",
        "KE": "肯尼亚",
        "CK": "库可群岛",
        "CW": "库拉索",
        "LV": "拉脱维亚",
        "LS": "莱索托",
        "LA": "老挝",
        "LB": "黎巴嫩",
        "LT": "立陶宛",
        "LR": "利比里亚",
        "LY": "利比亚",
        "LI": "列支敦士登",
        "RE": "留尼汪",
        "LU": "卢森堡",
        "RW": "卢旺达",
        "RO": "罗马尼亚",
        "MG": "马达加斯加",
        "IM": "马恩岛",
        "MV": "马尔代夫",
        "MT": "马耳他",
        "MW": "马拉维",
        "MY": "马来西亚",
        "ML": "马里",
        "MH": "马绍尔群岛",
        "MQ": "马提尼克岛",
        "YT": "马约特",
        "MU": "毛里求斯",
        "MR": "毛利塔尼亚",
        "US": "美国",
        "AS": "美属萨摩亚",
        "UM": "美属外岛",
        "VI": "美属维尔京群岛",
        "MN": "蒙古",
        "MS": "蒙特塞拉特",
        "BD": "孟加拉国",
        "PE": "秘鲁",
        "FM": "密克罗尼西亚",
        "MM": "缅甸",
        "MD": "摩尔多瓦",
        "MA": "摩洛哥",
        "MC": "摩纳哥",
        "MZ": "莫桑比克",
        "MX": "墨西哥",
        "NA": "纳米比亚",
        "ZA": "南非",
        "AQ": "南极洲",
        "GS": "南乔治亚和南德桑威奇群岛",
        "SS": "南苏丹",
        "NR": "瑙鲁",
        "NP": "尼泊尔",
        "NI": "尼加拉瓜",
        "NE": "尼日尔",
        "NG": "尼日利亚",
        "NU": "纽埃",
        "NO": "挪威",
        "NF": "诺福克岛",
        "PW": "帕劳群岛",
        "PN": "皮特凯恩群岛",
        "PT": "葡萄牙",
        "MK": "前南斯拉夫马其顿共和国 ",
        "JP": "日本",
        "SE": "瑞典",
        "CH": "瑞士",
        "SV": "萨尔瓦多",
        "WS": "萨摩亚",
        "RS": "塞尔维亚共和国",
        "YU": "塞尔维亚共和国, 黑山",
        "SL": "塞拉利昂",
        "SN": "塞内加尔",
        "CY": "塞浦路斯",
        "SC": "塞舌尔",
        "XS": "沙巴岛",
        "SA": "沙特阿拉伯",
        "BL": "圣巴泰勒米",
        "CX": "圣诞岛",
        "ST": "圣多美和普林西比",
        "SH": "圣赫勒拿、阿森松与特里斯坦达库尼亚",
        "KN": "圣基茨和尼维斯岛",
        "LC": "圣卢西亚",
        "SX": "圣马丁",
        "SM": "圣马力诺",
        "PM": "圣皮埃尔和密克隆群岛",
        "VC": "圣文森特和格林纳丁斯 ",
        "XE": "圣尤斯特歇斯岛",
        "LK": "斯里兰卡",
        "SK": "斯洛伐克",
        "SI": "斯洛文尼亚",
        "SJ": "斯瓦尔巴岛",
        "SZ": "斯威士兰",
        "SD": "苏丹",
        "SR": "苏里南",
        "SB": "所罗门群岛",
        "SO": "索马里",
        "TJ": "塔吉克斯坦",
        "TW": "台湾",
        "TH": "泰国",
        "TZ": "坦桑尼亚",
        "TO": "汤加",
        "TC": "特克斯和凯科斯群岛",
        "TA": "特里斯坦达昆哈",
        "TT": "特立尼达和多巴哥",
        "TN": "突尼斯",
        "TV": "图瓦卢",
        "TR": "土耳其",
        "TM": "土库曼斯坦",
        "TK": "托克劳",
        "WF": "瓦利斯和富图纳",
        "VU": "瓦努阿图",
        "GT": "危地马拉",
        "VE": "委内瑞拉",
        "BN": "文莱",
        "UG": "乌干达",
        "UA": "乌克兰",
        "UY": "乌拉圭",
        "UZ": "乌兹别克斯坦",
        "ES": "西班牙",
        "GR": "希腊",
        "HK": "香港特别行政区",
        "SG": "新加坡",
        "NC": "新喀里多尼亚",
        "NZ": "新西兰",
        "HU": "匈牙利",
        "SY": "叙利亚",
        "JM": "牙买加",
        "AM": "亚美尼亚",
        "XJ": "扬马延岛",
        "YE": "也门",
        "IQ": "伊拉克",
        "IR": "伊朗",
        "IL": "以色列",
        "IT": "意大利",
        "IN": "印度",
        "ID": "印度尼西亚",
        "UK": "英国",
        "VG": "英属维尔京群岛",
        "IO": "英属印度洋领地",
        "JO": "约旦",
        "VN": "越南",
        "ZM": "赞比亚",
        "JE": "泽西",
        "TD": "乍得",
        "GI": "直布罗陀",
        "CL": "智利",
        "CF": "中非共和国",
        "CN": "中国",

    }

    year_list=[
        #2018,
        #2017,
        #2016,
        #2015,
        #2014,
        #2013,
        #2012,
        #2011,
        #2010,
        #2009,
        #2008,
        #2007,
        #2006,
        #2005,
        #2004,
        #2003,
        #2002,
        #2001,
        #2000,
        #1999,
        #1998,
        1997,
        1996,
        1995,
        1994,
        1993,
        1992,
        1991,
        1990,
        1989,
        1988,
        1987,
        1986,
        1985,
        1984,
        1983,
        1982,
        1981,
        1980,
        1979,
        1978,
        1977,
        1976,
        1975,
        1974,
        1973,
        1972,
        1971,
        1970,
        1969,
        1968,
        1967,
        1966,
        1965,
        1964,
        1963,
        1962,
        1961,
        1960,
        1959,
        1958,
        1957,
        1956,
        1955,
        1954,
        1953,
        1952,
        1951,
        1950,
        1949,
        1948,
        1947,
        1946,
        1945,
        1944,
        1943,
        1942,
        1941,
        1940,
        1939,
        1938,
        1937,
        1936,
        1935,
        1934,
        1933,
        1932,
        1931,
        1930,
        1929,
        1928,
        1927,
        1926,
        1925,
        1924,
        1923,
        1922,
        1921,
        1920,
        1919,
        1918,
        1917,
        1916,
        1915,
        1914,
        1913,
        1912,
        1911,
        1910,
        1909,
        1908,
        1907,
        1906,
        1905

    ]
    Month_list=[
        1,2,3,4,5,6,7,8,9,10,11,12
    ]
    day_list=[
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31
    ]
    global userName, userPassword ,maprd # 为了便于后面使用，定义为全局变量
    userName = ''
    userPassword = ''
    myid=0
    maprd={id:1}
    def savefile(self):
        global maprd
        with open("%s.txt" % "ok_text", "a") as f:  # 格式化字符串还能这么用！
            f.write("%s@outlook.com === %s"%(maprd["MemberName"],maprd["PasswordInput"])+"\n")
            print "%s@outlook.com === %s"%(maprd["MemberName"],maprd["PasswordInput"])+"\n"
        with open("%s.txt" % "all_text", "a") as f:  # 格式化字符串还能这么用！
            f.write(json.dumps(maprd) +"\n")

    def get_userNameAndPassword(self):
        self.myid=self.myid+1
        global userName, userPassword,maprd
        # 8位用户名及6位密码
        pd=''.join(
            random.sample("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-><:}{?/", 11))
        un=''.join(random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 8))

        lastname = ''.join(random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", 5))

        FirstName = ''.join(random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", 3))
        userName =un
        userPassword =pd
        strzim="qazwsxedcrfvtgb yhnujmikopMNBVCXZPOIKJUYTREWQASDFGHJKL"
        n = random.randint(0, len(strzim)-1)#字母
        pp=strzim[n]
        strzim = "1234567890"
        n = random.randint(0, len(strzim)-1)#数字
        ppnum = strzim[n]
        print("随机前缀："+pp)  # 返回一个字符串随机位置的字符
        timexx=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print "开始时间：%s"%timexx
        maprd.clear();  # 清空词典所有条目
        maprd["id"]=self.myid
        maprd["time"]=timexx# 格式化成2016-03-20 11:45:39形式

        maprd["MemberName"]=pp+un
        maprd["PasswordInput"] = pp + pd+ppnum
        maprd["LastName"] = pp + lastname
        maprd["FirstName"] = pp +FirstName
        maprd["Country_k"] = self.country_list[random.randint(0, len(self.country_list)-1)]
        maprd["Country_v"] = self.country_map[ maprd["Country_k"]]
        maprd["BirthYear_k"] =self.year_list[random.randint(0, len(self.year_list)-1)]
        maprd["BirthYear_v"] =  maprd["BirthYear_k"]
        maprd["BirthMonth_k"] = str(self.Month_list[random.randint(0, len(self.Month_list)-1)])
        maprd["BirthMonth_v"] = maprd["BirthMonth_k"]+u"月"
        maprd["BirthDay_k"] = str(self.day_list[random.randint(0, len(self.day_list)-1)])
        maprd["BirthDay_v"] = maprd["BirthDay_k"]+u"日"
        print  maprd

        return maprd



    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):

        self.gogoreg()

    def gogoreg(self):
        #try:
        self.get_userNameAndPassword()
        print "用户名:", userName
        print "密码:", userPassword
        #except Exception, e:
        #    print e.message
        global  maprd

        driver = self.driver
        driver.get("https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1528799945&rver=6.7.6640.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3df55afda9-347d-ebc9-2a89-6b30da60ff18&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&uaid=18ddbce973ef45fbb3d2bf00ee1de667&lic=1")
        driver.find_element_by_id("MemberName").click()
        driver.find_element_by_id("MemberName").clear()
        driver.find_element_by_id("MemberName").send_keys(maprd["MemberName"])#"ed00997dcc9994fcv")
        driver.find_element_by_id("iSignupAction").click()
        driver.find_element_by_id("PasswordInput").click()
        driver.find_element_by_id("PasswordInput").clear()
        driver.find_element_by_id("PasswordInput").send_keys(maprd["PasswordInput"])#"577cca12wasas")
        driver.find_element_by_id("iSignupAction").click()
        driver.find_element_by_id("LastName").click()
        driver.find_element_by_id("LastName").clear()
        driver.find_element_by_id("LastName").send_keys(maprd["LastName"])#"sprintxxxz")
        driver.find_element_by_id("FirstName").clear()
        driver.find_element_by_id("FirstName").send_keys(maprd["FirstName"])#"printbbb")
        driver.find_element_by_id("iSignupAction").click()

        self.savefile()

        #print maprd["Country_v"],maprd["BirthYear_v"],maprd["Country_k"],maprd["BirthMonth_v"]
        #print maprd["Country_k"],maprd["BirthMonth_k"]
        select = driver.find_element_by_xpath("//select[@id='Country']")
        select.find_element_by_xpath("//option[@value='"+maprd["Country_k"]+"']").click()

        select = driver.find_element_by_xpath("//select[@id='BirthYear']")
        select.find_element_by_xpath("//option[@value='" + str(maprd["BirthYear_k"])+ "']").click()

        select = driver.find_element_by_xpath("//select[@id='BirthMonth']")
        if maprd["BirthMonth_k"] not in self.Month_list:
            maprd["BirthMonth_k"]="1"
        select.find_element_by_xpath("//option[@value='" + str(maprd["BirthMonth_k"]) + "']").click()
        print u'择天:',maprd["BirthDay_k"]
        time.sleep(3)
        if int(maprd["BirthDay_k"]) not in self.day_list:
            maprd["BirthDay_k"]="1"
        print maprd["BirthDay_k"]
        select = driver.find_element_by_xpath("//select[@id='BirthDay']")
        #maprd["BirthDay_k"]="6"
        if int(maprd["BirthDay_k"]) <13:
            #print ""
            #maprd["BirthDay_k"] = "13"
            select.find_elements_by_xpath("//option[@value='" + str(maprd["BirthDay_k"]) + "']")[1].click()
        else:
            select.find_element_by_xpath("//option[@value='" + str(maprd["BirthDay_k"]) + "']").click()
        #select.find_element_by_xpath("//option[@value='" + str(maprd["BirthDay_k"]) + "']").click()
        #select1 = driver.find_element_by_xpath("//select[@id='BirthDay']")
        #select1.find_element_by_xpath("//option[@value='%s']"%maprd["BirthDay_k"]).click()
        #driver.find_element_by_id("BirthDay").click()
        #Select(driver.find_element_by_id("BirthDay")).select_by_visible_text(maprd["BirthDay_v"])#u"11日")

        #driver.find_element_by_xpath("(//option[@value='"+maprd["BirthDay_k"]+"'])").click()
        #driver.find_element_by_xpath("(//option[@value='5'][1])").click()
        #select.find_element_by_xpath("//option[@value='" + str(maprd["BirthDay_k"]) + "']").click()
        #driver.find_element_by_id("Country").click()
        #Select(driver.find_element_by_id("Country")).select_by_visible_text(maprd["Country_v"])#u"直布罗陀")
        #driver.find_element_by_xpath("//option[@value='"+maprd["Country_k"]+"']").click()
        time.sleep(5)
        #driver.find_element_by_id("BirthYear").click()
        #Select(driver.find_element_by_id("BirthYear")).select_by_visible_text(str(maprd["BirthYear_v"]))#"2006")
        #pr=
        #print px
        #driver.find_element_by_xpath("//option[@value='"+str(maprd["BirthYear_k"])+"']").click()


        #time.sleep(3)
        #driver.find_element_by_id("BirthMonth").click()
        #Select(driver.find_element_by_id("BirthMonth")).select_by_visible_text(maprd["BirthMonth_v"])#u"5月")
        #driver.find_element_by_xpath("//option[@value='"+str(maprd["BirthMonth_k"])+"']").click()
        #driver.find_element_by_id("BirthDay").click()
        #Select(driver.find_element_by_id("BirthDay")).select_by_visible_text(maprd["BirthDay_v"])#u"11日")
        #driver.find_element_by_xpath("(//option[@value='"+maprd["BirthDay_k"]+"'])[2]").click()
        #time.sleep(5)
        driver.find_element_by_id("iSignupAction").click()
        #driver.find_element_by_id("LastName").click()
        #driver.find_element_by_id("LastName").clear()
        #driver.find_element_by_id("LastName").send_keys("bbcsz")
        #driver.find_element_by_id("iSignupAction").click()
        #driver.find_element_by_id("iSignupAction").click()
        #driver.find_element_by_id("wlspispSolutionElementeeb8129a0ee84ef58682f07250f815fe").click()
        #driver.find_element_by_id("wlspispSolutionElementeeb8129a0ee84ef58682f07250f815fe").clear()
        #driver.find_element_by_id("wlspispSolutionElementeeb8129a0ee84ef58682f07250f815fe").send_keys("vryhv3")
        print u'输入验证码120秒'
        time.sleep(120)
        driver.find_element_by_id("iSignupAction").click()

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
    #for num in range(1, 3):  # 迭代 10 到 20 之间的数字
    unittest.main()
