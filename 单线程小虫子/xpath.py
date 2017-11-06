# -*- coding:utf-8 -*-
import requests, re
from lxml import etree
# import sys, importlib
# importlib.reload(sys)
# sys.getdefaultencoding()

cookie = {
    # "Cookie": "_T_WM=53318b04d2da2cef633bef19056a0e8b; H5_INDEX=3; H5_INDEX_TITLE=IdenPin; ALF=1512443024; SCF=AuXQlhgGVR00IUgeHpBuB8ck-y9h2v4FkLQkXJ65QBQZLVsSyqdZwHMEgpravfSldB0D6C24eihsBLKXHXsMEvM.; SUB=_2A250-vJYDeRhGedG61YW9SzFwj-IHXVUBJ4QrDV6PUJbktANLVj7kW1v8wY6Jad47U15gNsRs68OQ0kXLQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWXjjCVa0kqy-LAHQxHoAwZ5JpX5K-hUgL.Fo2RehBNSKz41Ke2dJLoI7Ui9sHV-sLV; SUHB=0FQqzf4oNlVepc; SSOLoginState=1509851656"
}
html = requests.get('https://movie.douban.com/chart', cookies=cookie).content
selector = etree.HTML(html)
# content = selector.xpath('//div[@class="ctc box"]/div[@class="text"]/p/text()')
# content = selector.xpath('//div[@class="pic"]/a[@class="img"]/img/@src')
# content = selector.xpath('//div[start-with(@class,"list-item")]/text()')
content = selector.xpath('//div[@class="pl2"]/p/text()')
# print(selector.xpath('string(.)'))


f = open('content.txt', 'a', encoding='utf-8');
for index, each in enumerate(content):
    # text = each.xpath('string(.)')
    each = '第'+str(index+1)+'条：' + each + '\n'
    print("第"+str(index+1)+"条成功写入")
    f.write(each)
f.close()
