import re
import requests
from prettytable import PrettyTable

'''
   
   素拓分快速查询程序，
   运行前请在下方输入自己的账号和密码，
   确保网络为校园内网并运行程序快速查看。
   由于中英文字体宽度原因，显示结果不会对齐，强迫症者见谅。
    
'''

user = "2018030402055"  # 此处修改账号
psw = "252614"  # 此处修改密码


user_agent = {
    'Host': 'cas.zsc.edu.cn',
    'Origin': 'https://cas.zsc.edu.cn',
    'Referer': 'https://cas.zsc.edu.cn/login?service=http%3A%2F%2F210.38.224.229%2Fsuzhi%2FCASLogin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}


def login(sess, account, password):
    url = 'https://cas.zsc.edu.cn/login?service=http%3A%2F%2F210.38.224.229%2Fsuzhi%2FCASLogin'
    response = sess.get(url, headers=user_agent)
    cookie = response.cookies
    # print(res.text)
    page_source = response.text
    lt = re.findall(re.compile(r'<input type="hidden" name="lt" value="(.*?)" />', re.S), page_source)[0]
    et = re.findall(re.compile(r'<input type="hidden" name="execution" value="(.*?)" />', re.S), page_source)[0]
    login_data = {
        'username': account,
        'password': password,
        'lt': lt,
        'execution': et,
        '_eventId': 'submit'
    }
    response = sess.post(url=url, data=login_data, headers=user_agent, cookies=cookie)
    cookie = response.cookies

    return cookie


def get_content(sess, cookie):
    url = 'http://210.38.224.229/suzhi/student/authentication/authentication/authenticationList.jsp'
    response = sess.get(url, headers=user_agent, cookies=cookie)
    cookie = response.cookies
    data = {
        'itemPerPage': '30'
    }
    page_source = sess.post(url, headers=user_agent, cookies=cookie, data=data)

    return page_source


def parse_list_page(page_source):
    table = PrettyTable(['编号', '活动名称', '获得学分', '班级审核状态', '院系审核状态', '学校审核状态', '审核截止日期', '申报成功'])
    table.align = 'l'
    pattern = re.compile(r'<input type="checkbox" name="checkbox" value=".*?">.'
                         r'*?<td title=".*?">(.*?)</td>.*?<a href=.*?title="查看'
                         r'详细信息">(.*?)</a>.*?"查看详细信息".*?<span.*?title=".'
                         r'*?">(.*?)</span>.*?"查看详细信息".*?<span.*?title=".*?'
                         r'">(.*?)</span>.*?"查看详细信息".*?<span.*?title=".*?">'
                         r'(.*?)</span>.*?<td title=.*?>(.*?)</td>', re.S)

    page_source = page_source.text
    n_sum = 0.0
    text = re.findall(pattern, page_source)
    t_id = int(0)
    for t in text:
        t_id = t_id + 1
        flag = False
        if t[4] == "通过":
            flag = True
        n_sum += float(t[1])
        table.add_row([str(t_id), t[0], t[1], t[2], t[3], t[4], t[5], "是" if flag else "否"])
    table.add_row(["", "目前总共申报的分数:", round(n_sum, 2), "", "", "", "", ""])

    return table


def parse_score_page(sess):
    url = 'http://210.38.224.229/suzhi/stat/credit/creditStatStudent2.jsp'
    page_source = sess.get(url=url, headers=user_agent).text
    pattern = re.compile(r'<th colspan="2">(.*?)</th>.*?</tr>', re.S)
    text = re.findall(pattern, page_source)
    text = text[0]
    text.lstrip()
    s_sum = float(text.split()[0])
    s_str = '目前获得的总分为：%.2f' % s_sum

    return s_str


def main():

    sess = requests.session()
    cookie = login(sess, user, psw)
    page_source = get_content(sess, cookie)
    table = parse_list_page(page_source)
    score = parse_score_page(sess)

    print(table)
    print(score)


if __name__ == '__main__':
    main()

