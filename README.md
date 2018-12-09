

### 表格
属性 | 内容
---|---
Target release  | 2018/11/25
Epic            | 建立一个吸纳学习者的一个社区空间
Document status | 进行中
Document owner  | 陈荣城
Designer        | 陈荣城
Developer       | 陈荣城
QA              | 陈荣城
Edition         | 1.1




# Goals
- 通过多个API交互使用，降低用户使用成本，提高用户效率。
- 通过软件方便用户进行外语学习，使用户能够更加系统的学习英语，理解句子结构。赏析优秀的句子并仿写以提高自身能力水平。
- 建立一个用户交流的社区化软件。
- （1.1新增）通过分析用户的使用历史、查询内容，给用户推荐更加合适的优质内容。
- （1.1新增）利用现有的API接口，实现合并使用，将多个功能集成，减少用户一两秒的冗余操作。（如文本识别与文本翻译）

# Background and strategic fit
- 市面上使用最多的英语翻译工具功能繁琐，页面复杂，面对于多元化的用户，自定义设置的项目过少，只能通过开放数据下载包为不同客户制定单一的学习内容。
- 而且，对于工具的位置定位，随着时代的快节奏。首先安装包过于庞大，多数用户在没有形成产品依赖和品牌信任之前，容易提高入门门槛，不利于用户接触产品，产生产品体验。
- （1.1新增）市面上的翻译软件没有提供一个社区空间给用户进行交流，使得用户更像是独自学习。
- （1.1新增）市场上的翻译软件功能单一，并以推荐课程，让学生报名加入等方式，对于用户缺少更加智能化的优化体验。同时也在增加用户的学习成本。
- 在本产品里，初期只提供基本的单词、句子翻译功能以收藏复习功能，致力于对内容的优化，界面以及操作逻辑的跟进，先从高质量的实用工具角度进入市场。
- 中期开放扩展工具栏，开发多元化的模块以满足不同用户的需求，同时满足用户个性化定制的心理。除了开放官方模块，同时允许开发者自行开发模块，就像风靡至今的浏览器插件一般。
- （等时机）在前期中期时段，关注用户动态，开放社区系统，促进用户交流，增加用户粘性。1.（视情况）开放模块交流专区，利于官方对模块进行优化。同时给第三方开发者一个反馈的平台。2.增加读书交流专区，每日给出一段文章，就像看网络小说一样，有意识的培养用户每日登陆软件打卡的看书习惯。

# Assumptions
- 使用该产品的多为学生群体，主打年轻像，后期吸引大咖分享读书感言。
- 使用工具多为移动设备，但仍会有少量平板使用的可能。
- 使用场景多为对外语文本语义的查询，尤其是将要备战四六级考试的学生。
- 前期主打工具定位，即用时能快速切入，随后又能自动退出后台。操作逻辑简洁清晰，尽量去除干扰项。
- 后期主打用户粘性，以优秀的内容，生动有趣的社区空间留住用户。
- 对于整个产品，采取模块化建设，以小软件为基础，低入门门槛吸引用户，用用户所喜欢的模块留住用户。

# Requirements

N | Title | User story | Importance| Notes
---|---|---|---|---
  1 | 跨软件使用 |A用户正在阅读一本外国名著，遇到了不认识的句子，于是复制该句子，然后软件检测到剪切板有新内容增加，直接进行翻译，在顶部弹出长方形框，内容为翻译内容，翻译内容下面用着小一号的浅灰色字体显示翻译的原句|必须有|在弹出长方形框后，用户可以通过长按进入设置，设置为是否实时常驻后台，是否有进行翻译的需要 
  2      |文本识别 |B用户正在浏览杂志，发现配图下有着一句话，于是下拉通知栏，点击驻留在通知栏的软件快速查询按钮中的文字识别按钮，将内容置于扫描框内，若扫描框不够大，可以在右上角选择适合大小的扫描框，识别后回到软件结果显示结果。  |必须有 |   后台常驻是否能得到用户的许可，是否需要添加收藏功能以便用户日后复习查看结果         
  3|单词、句子和文章收藏    |用户在翻阅时遇到心仪的句子和文章时选择收藏，弹出账号登陆注册页，登陆后选择收藏目录，该目录可以自定义。|必须有|产品初期使用允许不进行账号登陆使用，此时只开放基础功能。登陆后可以享受模块下载记录，方便日后或者更换设备以便快速使用自己调配的功能。享受文章云收藏，社区评论等。
  （1.1新增）4 |    智能学习内容推荐系统   |  用户在自己平常的学习时间段内，想看一些外语名著或比较著名的书籍时，打开软件进入书籍推荐区，软件通过用户过去所查询过的单词，句子，句型结构，句子内容。通过分析词汇量，过去查询的句子内容类型，以及结合网络上对于书籍的热度，普及度还有评语分析，确认是否推荐书籍，用户接收到了推荐的书籍的书单，自行进行二次挑选，选择自己喜欢的书籍进行阅读。    |     必须有     |    经过系统推荐的书籍能根据用户的词汇量和外语水平，让用户能够在能力范围之内锻炼自己的外语能力。
  （1.1新增）5|     外语热点新闻    |   用户在空闲时刻，碎片的休息时间内，进入新闻板块，系统抓取热点的外国新闻，系统根据新闻的内容确定类型打上标签。根据报道的覆盖范围，浏览人数还有评语，确认该新闻是否具有推荐价值。最后将内容输出到新闻版面供用户选择浏览。用户能够浏览到有价值的，感兴趣的，同时又是具有普及度的新闻。    | 重要性一般  | 新闻的浏览能够让用户了解外国实时，更加贴近的从生活文化上去学习。介于有些用户对于新闻推荐有抵触情感，同时这个功能也不是刚需，所以这个版面可以做成一个可供用户选择安装的模块。交换选择权。
  

# User interaction and design
## 用户使用流程

![登录注册流程图.PNG](https://i.loli.net/2018/12/01/5c016907ba517.png)  
https://i.loli.net/2018/12/01/5c016907ba517.png

## 产品原型界面
![主界面.PNG](https://i.loli.net/2018/12/01/5c01784803cf8.png)  
主界面：https://i.loli.net/2018/12/01/5c01784803cf8.png

![翻译页.PNG](https://i.loli.net/2018/12/01/5c01784800b82.png)  
翻译页：https://i.loli.net/2018/12/01/5c01784800b82.png

# API展示区
### 百度通用API使用
- 注意使用自身申请的appid和密钥，以下为本人个人key，仅供试用。
- 在q='输入内容'修改输入项即可得出结果
``` python
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

```
### 百度通用文字识别
- 注意，使用时请自行申请access_token，一下为本人key,仅供试用。
- 修改‘##图片地址##’即可查看图片所含文字
```
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

```
# Questions

Below is a list of questions to be addressed as a result of this requirements document:

Question | Outcome
---|---
前期如何使软件在用户不使用时自动退出，以节省用户运行内存及电量，提高用户好感度 | 用户自定义设置，是否开启后台纯净模式。或者软件后台自动检测，未运行时间达到一个阈值时自动关闭，或者检测用户使用习惯，自动学习，在不同软件决定是否结束后台。 
|如何将软件尽可能的缩小体积，作为一款随用随开的便携工具。|后期软件设计师解决，同时对功能进行细致化的整理。以及考虑模块化功能的实现，将选择权交还给用户。
|对于权限的获取时机提出|以用户使用到该功能时弹出获取权限框，同时，当用户拒绝权限给予时，只会影响到权限相关的功能，其他功能不受影响。


# Not doing
- 不插入不相关类型的广告
- 不自动勾选软件更新，初次有软件更新时提醒。
- 

## 附件清单
- 登陆注册流程图：https://i.loli.net/2018/12/01/5c016907ba517.png
- 原型主界面：https://i.loli.net/2018/12/01/5c01784803cf8.png
- 原型翻译页：https://i.loli.net/2018/12/01/5c01784800b82.png
