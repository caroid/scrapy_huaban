# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class ScrapyJobPipeline(object):
    def process_item(self, item, spider):
        with open('php.csv', 'a', newline='') as f:
            spamwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE)
            spamwriter.writerow([item["jobName"], item["salary"], item["city"], item["experience"],
                                 item["company"], item["education"], item["location"] ])

        return item
