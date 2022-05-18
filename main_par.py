# #!/usr/bin/env python
# -*- coding: UTF-8 -*-
# On 2022/5/5 22:20 Debrnr used the main_par written by PyCharm on Gamer

from random import randint
from time import time
from urllib.parse import quote


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


class WebSiteParames(object):
    """ WebSiteParames 网站参数设置 """
    HEADER = {
        'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/100.0.4896.127 Safari/537.36'
    }
    # ---- IMG_SITE_URL
    URL = 'https://image.baidu.com/search/acjson'
    # ---- URL_PAR
    PARS = {
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
    PARS_SETTING = 'word,pn'

    def __init__(self):
        self.url = WebSiteParames.URL
        self.parames = WebSiteParames.PARS
        self.headers = WebSiteParames.HEADER
        self.set = WebSiteParames.PARS_SETTING

    def generate_the_url(self, *args):
        set = self.set.split(',') if self.set.split(',') else list(self.set)
        if len(args) > 0:
            for key, velue in zip(set, args):
                print(velue)
        #         self.parames[key] = velue if velue.isdigit() or velue.isalpha() else quote(velue)
        # return self.url + '?' + '&'.join(i.strip() for i in ['{}={}'.format(i,j) for i,j in self.parames.items()])

    @classmethod
    def headers(cls):
        return cls.HEADER

    @classmethod
    def wurl(cls, par=None):
        cls.URL = par

    @classmethod
    def wparames(cls, par=None):
        cls.PARS = par

    @classmethod
    def wheaders(cls, par=None):
        cls.HEADER = par

    @classmethod
    def wset(cls, par=None):
        cls.PARS_SETTING = par


if __name__ == '__main__':
    wsp = WebSiteParames()
    print(wsp.generate_the_url('天启,2'))
