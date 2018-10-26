# -*- coding:utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# qiweb 20180902 16:26
# 读取数据实现增删改查api接口
'''
pip install
Flask==1.0.2
Flask-API==1.0
Flask-HTTPAuth==3.2.4
Flask-RESTful==0.3.6
PyYAML==3.13
'''
# 使用 Python 和 Flask 设计 RESTful API
# GET         http://[hostname]/qiweb/             欢迎
# GET         http://[hostname]/qiweb/updateip 跟换tor的ip


import os
from flask import Flask, jsonify, make_response



app = Flask(__name__)



@app.route('/qiweb/updateip', methods=['GET'])
def updateip():
    # 我们使用    JSON    数据格式来响应，Flask    的    jsonify    函数从我们的数据结构中生成。
    print "Running tests... ip chege"
    os.system("""(echo authenticate '"mypassword"'; echo signal newnym; echo quit) | nc localhost 9051""")
    # 转换id 成url比较直观
    return jsonify({'qiweb': "ip update successful"})


# $ curl -i http://localhost:5000/qiweb/api/v1.0/tasks




# 欢迎首页
@app.route('/')
def index():
    return make_response(jsonify({'qiweb-linux_server': 'Hello, World!', 'hi': 'welcome to python flask restful api for qiweb'}))
    # return "Hello, World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
    # app.run()
