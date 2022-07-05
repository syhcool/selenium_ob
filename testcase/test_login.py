# -*- coding:utf-8 -*-
# user:syh
from page_object.login import Login
import pytest
from config.Conf import Config_Yaml
import allure

@allure.feature("登录测试")
class Test_Login:
    data = Config_Yaml().get_login_data()
    @pytest.mark.parametrize("name,password,exce",data)
    # @allure.title("{title}")
    def test_login(self,name,password,exce):
        assert Login().login(name,password) == exce


if __name__ == '__main__':
    pytest.main(['-vs','test_login.py'])
