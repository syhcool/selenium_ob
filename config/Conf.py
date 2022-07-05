# -*- coding:utf-8 -*-
# user:syh
import datetime
import os
#设置主目录
from common.YamlReader import YamR

current = os.path.dirname(os.path.dirname(__file__))
#获取当前时间
current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#定义config目录的路径
_config_path = current + os.sep +"config"

#设置日志文件路径
_log_path = current + os.sep +"outputs\logs"
#设置截图文件路径
_screenshot_path = os.path.join(current + "\outputs\screenshot\\" + current_time + '.png')
#设置用例文件路径
_testdata_path = current + os.sep + 'testdata'
#设置登录用例文件
_login_file = _testdata_path + os.sep + 'TestLogin.yaml'

def get_log_path():
    return _log_path
def get_screenshot_path():
    return _screenshot_path
def get_config_path():
    return _config_path
def get_login_file():
    return _login_file

class Config_Yaml():
    def get_login_data(self):
        return YamR(get_login_file()).data()
if __name__ == "__main__":
    print(Config_Yaml().get_login_data())