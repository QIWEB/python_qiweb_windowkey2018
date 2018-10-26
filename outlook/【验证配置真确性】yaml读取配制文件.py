# -*- coding:utf-8 -*-
import yaml
import os
#验证配置文件对不对
# 作者：上海-qiweb 交流QQ：908701702

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件路径
yamlPath = os.path.join(curPath, "qiwebkeyConfig.yaml")
yamlPath = "qiwebkeyConfig.yaml"
# open方法打开直接读出来
f = open(yamlPath, 'r')
cfg = f.read()
print(type(cfg))  # 读出来是字符串
print(cfg)

d = yaml.load(cfg)  # 用load方法转字典
print( d)
a=d["qiweb"]
for  key in a:
    #print(key + ':' )
    #print a[key]
    valus=a[key]
    #是int说明配置的了数量
    if isinstance(valus,int)  and int(valus)>0:
        #循环提取
        for i in range(0,int(valus)):
            #把所有的_替换成空格
            print  key.replace('_',' ')
print u'配置文件正确'
#print(type(d))




def check_str(value):
    # 检查你输入的是否是字符类型
    if isinstance(value, str):
        # 判断字符串以什么结尾
        if value.endswith('.sh'):
            return '%s 是以.sh结尾的字符串' % value
        # 判断字符串以什么开头
        elif value.startswith('xi'):
            return '%s 是以xi开头的字符串' % value
        else:
            return '%s 不满足以上条件的字符串' % value
    else:
        return '%s is not str' % value