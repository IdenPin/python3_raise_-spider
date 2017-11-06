import requests
from lxml import etree


# 泡菜君（雨妹）
# url = "http://dianely.lofter.com/"
url = "http://weibo.cn/u/2211085884"
wb_login_url = "https://passport.weibo.cn/signin/login"


login_data = {
    "username": "vipdengping@163.com",
    "password": "An635639654",
    "savestate": 1,
    "r": '',
    "ec": 0,
    "pagerefer": '',
    "entry": "mweibo",
    "wentry": "",
    "loginfrom": "",
    "code": "",
    "qq": "",
    "mainpageflag": 1,
    "hff": "",
    "hfp": ""
}

content = requests.post(wb_login_url, login_data)
# 设置编码防止乱码
def set_req_encoding():
    if content.encoding == 'ISO-8859-1':
        content.encoding = 'gbk'
    else:
        content.encoding = 'utf-8'
set_req_encoding()


print(content.text)







'''
http://blog.csdn.net/a491057947/article/details/47292923
text/html
ISO-8859-1
GB2312
返回的内容是采用‘ISO-8859-1’，所以出现了乱码，而实际上我们应该采用‘utf-8’编码
'''
# print(content.headers['content-type'])
# print(content.encoding)
# print(content.apparent_encoding)


