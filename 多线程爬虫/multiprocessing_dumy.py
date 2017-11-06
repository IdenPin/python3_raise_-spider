import requests, json
from multiprocessing.dummy import Pool as ThreadPool
from lxml import etree

# 写入
def towrite(lofter):
    f.writelines('Lofter标题：'+ str(lofter["title"])+'\n')
    f.writelines('Lofter热度：'+ str(lofter["hotnum"])+'\n')
    f.writelines('Lofter图片地址：'+ str(lofter["img"])+'\n')
    f.writelines('Lofter内容：'+ str(lofter["content"]).replace(',', '')+'\n\n')


def spider(url):
    html = requests.get(url).content
    selector = etree.HTML(html)
    content_field = selector.xpath('//div[@class="main"]')
    item = {}
    for each in content_field:
        lofter_title = each.xpath('h2/a/text()')
        lofter_content = each.xpath('//div[@class="text"]/p/text()')
        lofter_img = each.xpath('//div[@class="img"]/a/img/@src')
        lofter_hotnum = each.xpath('div[@class="link"]/a[2]/text()')
        if lofter_title == []:
            lofter_title = '默认标题'
        item["title"] = lofter_title
        item["content"] = lofter_content
        item["hotnum"] = lofter_hotnum
        item["img"] = lofter_img
        print(str(item) + '\n')
    towrite(item)

if __name__ == '__main__':
    pool = ThreadPool(4)
    f = open('lofter.txt', 'a', encoding='utf-8')
    page = []
    for i in range(1, 30):
        new_url = "http://dianely.lofter.com/?page=" + str(i)
        page.append(new_url)
    results = pool.map(spider, page)
    pool.close()
    pool.join()
    f.close()




