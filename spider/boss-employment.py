# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from prettytable import PrettyTable
import  lxml.html


class BossSpider(object):
    driver_path = 'chromedriver.exe'
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=BossSpider.driver_path)
        self.url = 'https://www.zhipin.com/c101280600/?query=C%2B%2B&ka=sel-city-101280600'
        self.base_url = 'https://www.zhipin.com'


    def run(self):
        self.driver.get(self.url)
        source = self.driver.page_source
        self.parse_link_page(source)


    def parse_link_page(self, source):
        pattern = re.compile('<h3 class="name">.*?<a href="(.*?)".*?>', re.S)
        links = re.findall(pattern, source)
        for link in links:
            detail_url = self.base_url + link
            self.driver.get(detail_url)
            detail_source = self.driver.page_source
            self.parse_detail_page(detail_source)
            break

    def parse_detail_page(self, source):
        # print(source)
        pattern = re.compile(r'<div class="name">.*?<h1>(.*?)</h1>.*?<span class="salary">(.*?)</span>.*?</div>', re.S)
        strs = re.findall(pattern, source)
        name = strs[0][0]
        salary = strs[0][1]
        pattern = re.compile(r'<div class="info-primary">.*?<p>(.*?)'
                             r'<em class="dolt"></em>(.*?)<em class="dolt"></em>(.*?)</p>', re.S)
        strs = re.findall(pattern, source)
        city = strs[0][0]
        exp = strs[0][1]
        edu = strs[0][2]
        company = re.findall(re.compile('<a ka="job-detail-company".*?>(.*?)</a>', re.S), source)
        company = company[1]
        company = re.sub(r'\s', '', company)

        detail = re.findall(re.compile(r'<div class="detail-content">'
                                       r'.*?<div class="text">(.*?)</div>', re.S), source)

        detail = re.sub('<br>', '\n', detail[0])
        detail = re.sub(r'^\s*', '', detail)
        # print(detail)
        job_detail = {
            'name': name,
            'company': company,
            'city': city,
            'salary': salary,
            'exp': exp,
            'edu': edu,
            'detail': detail
        }
        print(job_detail)


if __name__ == '__main__':
    spider = BossSpider()
    spider.run()
