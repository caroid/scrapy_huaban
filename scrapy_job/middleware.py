# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy.http import HtmlResponse
from selenium import webdriver
import time


class JavaScriptMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == "huaban":
            print("PhantomJS is starting...")

            driver = webdriver.PhantomJS()
            # 指定使用的浏览器
            # driver = webdriver.Firefox()
            # driver.set_window_size(1920, 10000)
            #
            # driver.get(request.url)
            # driver.save_screenshot("./naod.png")
            # time.sleep(5)
            # js = "var q=document.body.scrollTop=20000"
            # driver.execute_script(js)
            # driver.save_screenshot("./naod2.png")




            # js1 = "var q=document.body.scrollTop=100000"
            #
            #
            # driver.execute_script(js1)

            # 可执行js，模仿用户操作。此处为将页面拉至最底端。
            time.sleep(1)
            body = driver.page_source
            print ("访问"+request.url)

            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)


        else:
            return
