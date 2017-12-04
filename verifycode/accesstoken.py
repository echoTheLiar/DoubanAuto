# -*- coding: utf-8 -*-

import urllib2, json

# 替换为自己的开发者 KEY
API_KEY = ""
SECRET_KEY = ""


def get_access_token():
    # 获取百度AI开放平台的access_token

    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
           '&client_id=' + API_KEY + '&client_secret=' + SECRET_KEY
    request = urllib2.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()
    if content:
        content = json.loads(content)
    return content
