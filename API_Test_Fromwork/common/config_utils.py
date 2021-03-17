
#方法1
# class ConfigUtils():
#     @property #方法变成了属性方法
#     def HOST(self):
#         return 'api.weixin.qq.com'
#
# config=ConfigUtils()
#
# if __name__ == '__main__':
#     print(config.HOST)

#方法2
import configparser
import os
config_file_path=os.path.join(os.path.dirname(__file__),'..','conf','config.ini')
class ConfigUtils():
    def __init__(self):
        self.cfg_obj=configparser.ConfigParser()
        self.cfg_obj.read(config_file_path,encoding='utf-8')

    @property
    def HOST(self):
        value=self.cfg_obj.get('default','HOST')
        return value

config=ConfigUtils()
if __name__ == '__main__':
    print(config.HOST)