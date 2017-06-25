# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class ScrapyJobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = Field()           # 职位名称
    company = Field()           # 公司名称
    companyType = Field()       # 公司类型
    EmployeeNumber = Field()    # 员工数量
    city = Field()              # 城市
    location = Field()          # 地点
    jobLocation = Field()       # 工作地点
    salary = Field()            # 薪资范围
    experience = Field()        # 工作经验
    education = Field()         # 学历
    postTime = Field()          # 发布时间
    positionInfo = Field()      # 职位信息
    keyWord = Field()           # 关键字、加分项
