#/usr/bin/env python
#coding=utf8
 


import http.client
import hashlib
import json
import urllib
import random


appid = '20181201000241666' #你的appid
secretKey = 'A3yalexDWaTRG6XFx4PV' #你的密钥

 
httpClient = None
myurl = '/api/trans/vip/translate'
q = '输入内容'
fromLang = 'auto' #源语言设置，可为auto。
toLang = 'en' #输出语言设置
salt = random.randint(32768, 65536)

sign = appid+q+str(salt)+secretKey
sign = hashlib.md5(sign.encode()).hexdigest()
myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)
 
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print (response.read())
except Exception as e:
    print (e)
finally:
    if httpClient:
        httpClient.close()