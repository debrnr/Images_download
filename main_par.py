# #!/usr/bin/env python
# -*- coding: UTF-8 -*- 
# On 2022/5/5 22:20 Debrnr used the main_par written by PyCharm on Gamer

from random import randint
from time import time


class Dd(object):
    """ 数字位数获取,数字定义
        Digital definition: Dd
    """

    def __init__(self):
        pass

    @classmethod
    def timenum(cls, num=10):
        t = str(time()).split('.')
        if 0 <= num < 10:
            return t[0][:num]
        if num == 10:
            return t[0]
        if num > 10:
            # 时间数字最大位数15,大于的只有15位输出
            n = num - 10
            return t[0] + t[1][:n]

    @classmethod
    def rint(cls, num=1):
        return str(randint(int('0' * num), int('9' * num)))


HEADER = {
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/100.0.4896.127 Safari/537.36'
}

# ---- IMG_SITE_URL
BAIDU_IMG_URL = 'https://image.baidu.com/search/acjson'

# ---- URL_PAR
BAIDU_PAR = {
    'tn': 'resultjson_com',
    'logid': Dd.rint(19),
    'ipn': 'rj',
    'ct': '201326592',
    'is': '',
    'fp': 'result',
    'fr': '',
    'word': '',
    'queryWord': '',
    'cl': 2,
    'lm': -1,
    'ie': 'utf-8',
    'oe': 'utf-8',
    'adpicid': ' ',
    'st': -1,
    'z': '',
    'ic': 0,
    'hd': '',
    'latest': '',
    'copyright': '',
    's': '',
    'se': '',
    'tab': '',
    'width': '',
    'height': '',
    'face': 0,
    'istype': 2,
    'qc': '',
    'nc': 1,
    'expermode': '',
    'nojc': '',
    'isAsync': '',
    'pn': '',
    'rn': 30,
    'gsm': '1e',
    Dd.timenum(13): '',
}

if __name__ == '__main__':
    print(Dd.rint(19), len(Dd.rint(19)))
    print(Dd.timenum(13), len(Dd.timenum(13)))
    print(len('1651760807517'))
    print(BAIDU_PAR)
