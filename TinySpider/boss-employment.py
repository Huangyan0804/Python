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
from selenium.webdriver.chrome.options import Options
import csv


class BossSpider(object):
    driver_path = 'chromedriver.exe'

    def __init__(self):
        self.chrome_options = Options()
        #self.chrome_options.add_argument('headless')
        #self.chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(executable_path=BossSpider.driver_path, options=self.chrome_options)
        self.table = PrettyTable(['name', 'company', 'city', 'salary', 'exp', 'edu', 'details'])
        self.table.align['details'] = 'l'
        self.url = 'https://www.zhipin.com/c101280100/?query=C%2B%2B&page=1&ka=page-1'
        self.base_url = 'https://www.zhipin.com'
        self.filename = 'boss-zhipin-guangzhou.csv'
        with open(self.filename, "w", encoding='gb18030', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['name', 'company', 'city', 'salary', 'exp', 'edu', 'details'])

    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            self.parse_link_page(source)
            next_btn = re.findall(re.compile(r'<a href=".*?" ka="page-next" class="(.*?)">', re.S), source)
            self.print_table()
            if next_btn[0] == 'next disabled':
                break
            else:
                next_btn = self.driver.find_element_by_class_name('next')
                self.driver.implicitly_wait(10)
                next_btn.click()
        self.driver.quit()

    def parse_link_page(self, source):
        pattern = re.compile('<div class="job-primary">.*?<div class="info-primary">'
                             '.*?<h3 class="name">.*?<a href="(.*?)".*?>', re.S)
        links = re.findall(pattern, source)
        #print(links)
        for link in links:
            detail_url = self.base_url + link
            self.driver.execute_script("window.open('%s')" % detail_url)
            self.driver.switch_to.window(self.driver.window_handles[1])
            detail_source = self.driver.page_source
            self.parse_detail_page(detail_source)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

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
        self.table.add_row(job_detail.values())

        # 将数据写在csv文件中
        self.save_job_data(job_detail)

    def save_job_data(self, job_detail):
        with open(self.filename, "a+", encoding='gb18030', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, job_detail.keys())
            writer.writerow(job_detail)

    def print_table(self):
        print(self.table)
        self.table.clear_rows()


if __name__ == '__main__':
    spider = BossSpider()
    spider.run()
