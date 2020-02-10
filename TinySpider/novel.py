# -*- coding:utf-8 -*-
import requests
import re
from selenium import webdriver

base_url = 'http://www.xbiquge.la'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                  '/74.0.3729.169 Safari/537.36',
    'Referer': 'http://www.xbiquge.la/13/13959/',
    'Host': 'www.xbiquge.la',
    'Cookie': '_abcde_qweasd=0; _abcde_qweasd=0; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1560395314;'
              ' bdshare_firstime=1560395313977; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1560396302'
}


driver_path = r'D:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('http://www.xbiquge.la/13/13959')

page_source = driver.page_source
pattern = re.compile(r'<dd>.*?<a href="(.*?)">(.*?)</a>.*?</dd>', re.S)
units = re.findall(pattern, page_source)

i = 1

for unit in units:
    url = unit[0]
    title = unit[1]
    title = re.sub(' .*', '', title)
    novel_url = base_url + url
    driver.get(novel_url)
    pattern = re.compile(r'<div id="content">(.*?)</div>', re.S)
    contents = re.findall(pattern, driver.page_source)
    novel_file = open(r'novels/' + title + '.txt', 'w')

    for content in contents:
        content = re.sub('<br>', '\n', content)
        content = re.sub('<.*?>', '', content)
        content = re.sub('&nbsp;', ' ', content)
        novel_file.write(content)

    i = i + 1

    if i == 10:
        break

#print(driver.page_source)

driver.quit()
