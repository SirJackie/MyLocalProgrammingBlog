from bottle import route, run, request, static_file
import json


# 首页
@route('/')
def index():
    return static_file('index.html', root='.')


# AJAX请求处理
@route('/ajax', method='POST')
def ajax():
    name = request.forms.get('name')
    message = 'Hello, {}!'.format(name)
    response = {'message': message}
    return json.dumps(response)


# 静态文件路由
@route('/<filename:path>')
def static(filename):
    return static_file(filename, root='.')


# 启动Web服务器
run(host='localhost', port=8000, debug=True)
