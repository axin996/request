import os
import configparser
config_file_path=os.path.join(os.path.dirname(__file__),'..','conf','config.ini')
print(config_file_path)

cfg_obj=configparser.ConfigParser()
cfg_obj.read(config_file_path,encoding='utf-8')
value=cfg_obj.get('default','HOST')
print(value)