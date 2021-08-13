# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/13 12:55
@Auth ： cainiao
@File ：test01_mp.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import api
from api.api_mp import ApiMp


class TestMp:
    #初始化
    def setup_class(self):
        #获取ApiMp对象，方便下面两个测试方法里使用
        self.mp = ApiMp()
    #测试登录接口
    def test01_mp_login(self,mobile,pwd):
        rep = self.mp.api_mp_login(mobile,pwd)
        print("登录的返回结果为：",rep.json())
        #提取返回的token
        token = rep.json().get("data").get("token")
        #把token添加到headers中
        api.headers['Authorization'] = "Bearer "+token
        assert 201 == rep.status_code
        assert "OK" == rep.json().get("message")

    #测试发布文章接口
    def test02_mp_article(self):
        rep = self.mp.api_mp_article()
        print(rep.json())
