# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import json
#url = 'http://210.38.224.229/suzhi/student/authentication/authentication/authenticationList.jsp'


login_header = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
                  ' like Gecko) Chrome/74.0.3729.169 Safari/537.36',

}

post_data = {
    'itemPerPage': '30'
}


def login(url, lt, exe, r_session):
    login_data = {
        'username': '2018030402055',
        'password': '252614',
        'lt': lt,
        'execution': exe,
        '_eventId': 'submit',
    }
    response = r_session.post(url, data=login_data, headers=login_header)
    print(response.cookies)
    return response


def get_login_web(url):
    r_session = requests.Session()
    page = r_session.get(url, headers=login_header)
    pattern1 = re.compile(r'<input type="hidden" name="lt" value="(.*?)" />', re.S)
    pattern2 = re.compile(r'<input type="hidden" name="execution" value="(.*?)" />', re.S)
    exe = re.findall(pattern2, page.text)[0]
    lt = re.findall(pattern1, page.text)[0]
    login_res = login(url, lt, exe, r_session)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
                      ' like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Referer': 'http://210.38.224.229/suzhi/index.jsp',
        'Upgrade - Insecure - Requests': '1'
    }

    turl = 'http://210.38.224.229/suzhi/student/authentication/authentication/authenticationList.jsp'
    res = r_session.get(turl, headers=header, cookies=login_res.cookies)
    print(res.text)

if __name__ == '__main__':
    login_url = 'http://210.38.224.229/suzhi/CASLogin'
    get_login_web(login_url)