# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import sys
from prettytable import PrettyTable
from prettytable import DEFAULT
import json
url = 'http://jwgln.zsc.edu.cn/jsxsd/xk/LoginToXk'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/61.0.3163.100 Safari/537.36',

}

post_data = {
    'encoded': 'MjAxODAzMDQwMjA1NQ==%%%enNxZmh5ODA0'
}
r_session = requests.session()
r_session.post(url, headers=header, data=post_data)
response = r_session.get('http://jwgln.zsc.edu.cn/jsxsd/grxx/xsxx', headers=header, cookies=r_session.cookies)
print(response.text)
