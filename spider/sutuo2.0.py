
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
import sys

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver_path = r'chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)


url = 'http://210.38.224.229/suzhi/student/authentication/authentication/authenticationList.jsp'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/61.0.3163.100 Safari/537.36',
    'Cookie': '3=1; 7=1; 10=1; 13=1; 16=1; JSESSIONID=860EAFC90A0BFC1B2918B976EE651DA8'
}


def login(drive):
    actions = ActionChains(drive)
    name_input = drive.find_element_by_id('username')
    actions.move_to_element(name_input)
    actions.send_keys_to_element(name_input, '2018030402055')  # 2018030103124

    psw_input = drive.find_element_by_id('password')
    actions.move_to_element(psw_input)
    actions.send_keys_to_element(psw_input, '252614')  # 202348
    actions.perform()
    submit_button = drive.find_element_by_xpath('//*[@id="fm1"]/input[3]')
    submit_button.click()


def wait(drive, name):
    try:
        element = WebDriverWait(drive, 20).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, name))
        )
    finally:
        driver.quit()



driver.get(url)

login(driver)
driver.get(url)
driver.implicitly_wait(10)
selectTag = Select(driver.find_element_by_xpath(r'//*[@id="pageForm"]/table[4]/tbody/tr/td[2]/span/select[1]'))
selectTag.select_by_index(2)


pattern = re.compile(r'<input type="checkbox" name="checkbox" value=".*?">.*?<td title=".*?">(.*?)</td>.*?<a href=.'
                     r'*?title="查看详细信息">(.*?)</a>.*?"查看详细信息".*?<span.*?title="'
                     r'.*?">(.*?)</span>.*?"查看详细信息".*?<span.*?title="'
                     r'.*?">(.*?)</span>.*?"查看详细信息".*?<span.*?title="'
                     r'.*?">(.*?)</span>.*?<td title=.*?>(.*?)</td>', re.S)


page_source = driver.page_source
text = re.findall(pattern, page_source)



n_sum = 0.0
table = PrettyTable(['编号', '活动名称', '获得学分', '班级审核状态', '院系审核状态', '学校审核状态', '审核截止日期', '申报成功'])

table.align = 'l'
t_id = int(0)
for t in text:
    t_id = t_id + 1
    flag = False
    if t[4] == "通过":
        flag = True
    n_sum += float(t[1])
    table.add_row([str(t_id), t[0], t[1], t[2], t[3], t[4], t[5], "是" if flag else "否"])





url = 'http://210.38.224.229/suzhi/stat/credit/creditStatStudent2.jsp'
driver.get(url)
page_source = driver.page_source
pattern = re.compile(r'<th colspan="2">(.*?)</th>.*?</tr>', re.S)
text = re.findall(pattern, page_source)
text = text[0]
text.lstrip()

s_sum = float(text.split()[0])


n_str = '目前申报的总分为：%.2f' % n_sum

s_str = '目前获得的总分为：%.2f' % s_sum

print(table)
print(n_str)
print(s_str)

driver.quit()

