#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
import time
import re

"""

    自用淘宝评论查询

"""


user_agent = {
    'accept': r'*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Referer': 'https://item.taobao.com/item.htm?spm=a230r.1.14.1.441f4d79aUV60H&id=521627870837&ns=1&abbucket=5',
    'Upgrade-Insecure-Requests': '1',
    "cookie": "_m_h5_tk=62e7cd6ed4d5119ec8761643021cb651_1581234637880; _m_h5_tk_enc=a09378dd03134a65e5b180bf5396b259; thw=cn; v=0; cookie2=167ccffe517a2bff7957fcea7df0d4cd; t=269d7e5593a1fe6a90bfea06b52ad664; _tb_token_=e3851330b33ef; cna=CLW5FqivsnsCAX1/P+Fsmi0l; _samesite_flag_=true; lgc=z749887292; dnk=z749887292; tracknick=z749887292; tg=0; unb=2691413687; uc3=nk2=GZ%2FoGNn6c1dTEQ%3D%3D&vt3=F8dBxdsbC08E%2BjcjzLI%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&id2=UU6oKI9%2FYwR75Q%3D%3D; csg=1c51dbb0; cookie17=UU6oKI9%2FYwR75Q%3D%3D; skt=c36993caa36935bf; existShop=MTU4MTMxMTQzMA%3D%3D; uc4=id4=0%40U2xlpsI7R9TKXWWTXuX1gVXbjbVc&nk4=0%40G1aRzVXz%2FOrrMfG2xw59PkdRfj4t; _cc_=URm48syIZQ%3D%3D; _l_g_=Ug%3D%3D; sg=271; _nk_=z749887292; cookie1=BxY4nmUX9Gu6itkkGggZTLab4JKvj%2BRzppU66PZohsE%3D; enc=Y8T9BtloRkmy6mta%2FTjUjqLYmohSkv41iQH2%2B8tyuASmhEQwvRj7ayK4byHRsDzatl6%2BNqfBGsc6neOsAUufQQ%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=32_1; uc1=cookie14=UoTUO8P5Sp21kA%3D%3D&lng=zh_CN&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&existShop=false&cookie21=UIHiLt3xThH8t7YQoFNq&tag=8&cookie15=W5iHLLyFOGW7aA%3D%3D&pas=0; x5sec=7b22726174656d616e616765723b32223a22393433373463623236643637623438353636613632373232656638366630323543493777672f4946454e2b582f2f364f754f6d2f76774561444449324f5445304d544d324f4463374d513d3d227d; l=cBx9qZRrQbNt1aX3BOfaKurza7JNzBOf1hFzaNbMiICPOZCAJcvOWZVAWGYJCnFVLsn9R3r4ZfqaBkY_Cy4ohEGfIqlBs2JN.; isg=BJeXt9iBha7NxgEiPEGDJbsiJgLh3Gs-WpUH--nD4mfVGLJa8a7rj2p-e_joukO2",
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
}


def main():
    r_session = requests.session()
    file = open('comment.txt', 'x')
    for i in range(1, 50):
        print('-'*20 + str(i) + '-'*20)
        url = "https://rate.taobao.com/feedRateList.htm?auctionNumId=521627870837&userNumId=914019985&currentPageNum={}&pageSize=20&rateType=&orderType=sort_weight&attribute=&sku=&hasSku=false&folded=0&ua=098%23E1hv2vvWvRhvUpCkvvvvvjiPn2zW1jiWRschtjEUPmPU6j1PnLzhgjYRPFcWQji2RUhCvv14cy6vwr147Dieja%2FjvpvhvUCvp2yCvvpvvhCvvphvC9mvphvvvUyCvvOCvhEvgWmivpvUvvCCWfp7bcmtvpvIvvCvxpvvvvvvvhW3vvvCJpvvBo6vvUjnvvCHbvvv9wWvvhZ%2BvvmCpQyCvhQme0xDjfVAnqWT8CNW0EAfjXrlBf2XrqpAhjCbFO7t%2B3v4J9kx6fItn1vDNr1l5d8re361D704diTAVA1l%2Bb8reTtYVVzZd34Adch%2B2QhvCvvvvvm5vpvhvvCCB86Cvvyvv9ZvRQvv9YWtvpvhvvCvpv%3D%3D&_ksTS=1581311891386_1244&callback=jsonp_tbcrate_reviews_list".format(i)
        response = r_session.get(url, headers=user_agent)
        j_str = response.text
        patten = re.compile('content":"(.*?)"', re.S)
        items = re.findall(patten, j_str)
        pre_str = ""
        for item in items:
            if item == pre_str:
                continue
            pre_str = item
            print(item)
            file.writelines(item+"\n")
        time.sleep(1)
    file.close()


if __name__ == '__main__':
    main()
