"""
启动命令：scrapy crawl 51job
启动shell：scrapy shell "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
"""

import scrapy
from ..items import ScrapyJobItem
from selenium import webdriver


class _51jobSpider(scrapy.Spider):
    name = "51job"
    allowed_domains = ["51job.com"]
    start_urls = [
        "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=030400&keyword=php&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9"
    ]



    def parse(self, response):

        sel = response.xpath('//*[@id="resultList"]/div[@class="el"]/p/span/a')

        for data in sel:
            titles = data.xpath('@title').extract()
            hrefs = data.xpath('@href').extract()
            for title, href in zip(titles, hrefs):
                if "php" in title.lower():
                    yield scrapy.Request(href, callback=self.job_page_parse)

        yield self.get_next_page(response)

    def get_next_page(self, response):
        sel_next_page = response.xpath('/html/body/div[2]/div[6]/div/div/div/ul/li[contains(@class, "bk")]/a')
        for nextPage in sel_next_page:
            if '下一页'==nextPage.xpath('text()').extract_first():
                link = nextPage.xpath('@href').extract_first()
                if link:
                    return scrapy.Request(link, callback=self.parse)
                else:
                    return None

    def job_page_parse(self, response):
        item = ScrapyJobItem()
        item["jobName"] =  response.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/h1/@title').extract_first() or ""
        if 'php' not in item["jobName"].lower():
            return None
            # raise CloseSpider('Not Found')

        item["company"] = response.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/p[1]/a/@title').extract_first() or ""
        item["salary"] = response.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/strong/text()').extract_first() or ""
        item["city"] = response.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/span/text()').extract_first().\
            split('-')[0] or ""
        item["location"] = ''.join(response.xpath('/html/body/div[2]/div[2]/div[3]/div[5]/div/p/text()').extract()).\
            replace('\t', '').replace('\r', '').replace('\n', '') or ""

        item["experience"] = ""
        item["education"] = ""
        item["postTime"] = ""
        for sel in response.xpath('/html/body/div[2]/div[2]/div[3]/div[1]/div/div/span'):
            ix = sel.xpath('em/@class').extract_first()
            data = sel.xpath('text()').extract_first()
            if 'i1' == ix:
                item["experience"] = data
            elif 'i2' == ix:
                item["education"] = data
            elif 'i3' == ix:
                pass
            elif 'i4' == ix:
                item["postTime"] = data

        yield item


class huabanSpider(scrapy.Spider):
    name = "huaban"
    allowed_domains = ["huaban.com"]
    start_urls = [
        "http://huaban.com/boards/29132115/"
    ]

    def parse(self, response):
        # print(response.body)


        # print(response.xpath('//*[@id="waterfall"]/div[1]/p[1]').extract() )

        sel = response.xpath('//*[@id="waterfall"]/div[contains(@class,"pin")]')
        print(":::::::::::::::::::::::::::::::::::::::::::::::")
        print(sel)
        print(":::::::::::::::::::::::::::::::::::::::::::::::")
        for data in sel:

            # print("________________________")
            titles  = data.xpath('a[contains(@class,"img")]/img/@src').extract()
            titles2 = data.xpath('a[contains(@class,"img")]/img/@alt').extract()
            titles3 = data.xpath('p[1]/text()').extract()
            # hrefs = data.xpath('/p').extract()
            #
            print(titles, titles2, titles3 )





