# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/13 21:48
@Auth ： cainiao
@File ：api_app.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import api
import requests
import time
class ApiApp:
    #初始化
    def __init__(self):
        self.url_login = api.host+""
        self.url_article = api.host+""
    #调用登录接口
    def api_app_login(self,phone,pwd):
        data = {"phone":phone,"pwd":pwd}
        return requests.post(self.url_login,json=data,headers = api.headers)
    #调用查询频道下的所有文章接口
    def api_app_article(self,channel_id,):
        data = {"channel_id":channel_id,"timestamp":int(time.time())}
        return requests.get(self.url_article,params=data,headers = api.headers)
