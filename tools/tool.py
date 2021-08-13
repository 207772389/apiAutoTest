# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/13 20:30
@Auth ： cainiao
@File ：tool.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import api
class Tool:
    #提取token
    @classmethod
    def common_token(cls,rep):
        #提取token
        token = rep.json().get("data").get("token")
        #追加请求信息头
        api.headers['Authorization'] = "Bearer "+token
    @classmethod
    def common_assert(cls,rep,status_code=201):
        assert status_code == rep.status_code
        assert "OK" == rep.json().get("message")