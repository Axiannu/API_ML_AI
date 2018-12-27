import urllib3,base64
from urllib.parse import urlencode
access_token='24.9b48b9e1c17a5a90bfe3a0525df40645.2592000.1546198061.282335-11538987' #该处请自行申请并填入
http=urllib3.PoolManager()
url='https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token='+access_token
f = open('##图片地址##','rb')
#参数image：图像base64编码
img = base64.b64encode(f.read())
params={'image':img}
#对base64数据进行urlencode处理
params=urlencode(params)
request=http.request('POST', 
                      url,
                      body=params,
                      headers={'Content-Type':'application/x-www-form-urlencoded'})
#对返回的byte字节进行处理。Python3输出位串，而不是可读的字符串，需要进行转换
result = str(request.data,'utf-8')
print(result)