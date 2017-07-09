# -*-coding:utf-8-*-
import sys
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from njupt.items import TestItem
reload(sys)
sys.setdefaultencoding("utf-8")
class ListSpider(CrawlSpider):
    # 爬虫名称
    name = "test"
    # 设置下载延时
    download_delay = 1
    # 允许域名
    allowed_domains = ["news.cnblogs.com"]
    # 开始URL
    start_urls = [
         "https://news.cnblogs.com"
        ]
    # 爬取规则,不带callback表示向该类url递归爬取
    rules = (
    Rule(SgmlLinkExtractor(allow=(r'https://news.cnblogs.com/n/page/\d',))),
    Rule(SgmlLinkExtractor(allow=(r'https://news.cnblogs.com/n/\d+',)), callback='parse_content'),
         )
  # 解析内容函数

    def parse_content(self, response):
        item = TestItem()
        # 当前URL
        title = response.selector.xpath('//div[@id="news_title"]/a/text()')[0].extract().decode('utf-8')
        item['title'] = title
        author = response.selector.xpath('//div[@id="news_info"]/span/a/text()')[0].extract().decode('utf-8')
        item['author'] = author
        view = response.selector.xpath('//div[@id="news_body"]/p/text()')[0].extract().decode('utf-8')
        item['view'] = view
        releasedate = response.selector.xpath('//div[@id="news_info"]/span[@class="time"]/text()')[0].extract().decode('utf-8')
        item['releasedate'] = releasedate
        yield item