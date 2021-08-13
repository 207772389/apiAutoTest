# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/13 12:45
@Auth ： cainiao
@File ：api_mp.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import requests

import api


class ApiMp:
    """把一个模块里要测试的接口都放在一个模块里，如：登录相关的（注册账号，登录等接口）放在一个模块里"""
    #初始化
    def __init__(self):
        #登录接口url
        self.login_url = api.host+"/a/b"
        #发布文章接口url
        self.article_url = api.host+"/c/d"
    #登录接口
    def api_mp_login(self,mobile,pwd):
        #定义请求参数
        data = {"mobile":mobile,"pwd":pwd}
        #调用post请求
        #这里记得返回结果！！！
        return requests.post(self.login_url,json=data,headers = api.headers)
    #发布文章接口 这里类似就不再写了
    def api_mp_article(self):
        #定义请求参数
        #调用post方法
        pass