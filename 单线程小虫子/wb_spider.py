import requests
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool



# 泡菜君（雨妹）
# url = "http://dianely.lofter.com/"
# url = "http://weibo.cn/u/2211085884"
cookie = {
    "cookies": "_T_WM=7b3cd531946361f12f10512778f97713; SCF=AqTnLqkKsHw3QaSd1Uw1aZCmW9Bnj2aaiI6kEvkqFb9fQcWo99K5G2SUuHGLGfYf0QhdAghfPDc8BLpoS06O7q8.; H5_INDEX=3; H5_INDEX_TITLE=IdenPin; SUB=_2A250-4psDeRhGedG61YW9SzFwj-IHXVUBxYkrDV6PUJbkdAKLVnGkW2bIxiwwpdQ4eqhn9lR-zOrWTHyCA..; SUHB=0N20NFsZ5wjLH8; SSOLoginState=1509947964; M_WEIBOCN_PARAMS=luicode%3D20000174%26uicode%3D20000174"
}


def spider(url):
    # 发起爬虫请求

    content = requests.post(url, cookies=cookie)
    # 设置编码防止乱码
    if content.encoding == 'ISO-8859-1':
        content.encoding = 'gbk'
    else:
        content.encoding = 'utf-8'
    selector = etree.HTML(content.content)
    selector = selector.xpath('//div[@class="c"]/div/span[@class="ctt"]')
    for index, each in enumerate(selector):
        each = each.xpath('string(.)').replace(" ", "").replace("\\n", "").replace("\\r", "").replace('"', "")
        if each != '':
            each = "第" + str(index + 1) + "条微博：" + each + '\r'
            print(each)
        f.writelines(each)
if __name__ == '__main__':
    pool = ThreadPool(4)
    f = open('yumei.txt', 'a', encoding='utf-8')
    page = []
    for i in range(1, 40):
        new_url = "http://weibo.cn/u/2211085884?page=" + str(i)
        page.append(new_url)
    results = pool.map(spider, page)
    print('雨妹微博爬取结束 ...')
    pool.close()
    pool.join()
    f.close()
























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


