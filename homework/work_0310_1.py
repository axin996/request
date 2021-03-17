import requests
import re
import json
from collections import OrderedDict #有序字典
# requests对form-date数据兼容性不太支持
# 传字典的方式 data=
# 传文件的方式 file=
host='47.107.178.45'
session1=requests.session()
url_value={
    'm':'u',
    'c':'register'
}
response1=session1.get(url='http://%s/phpwind/index.php'%host,
                       params=url_value)
response1_date=response1.content.decode('utf-8')
token=re.findall('name="csrf_token" value="(.+?)"/>',response1_date)[0]
print(token)

url_params={
    'm':'u',
    'c':'login',
    'a':'dologin'
}
url_info={
    'username':'test02',
    'password':'123456',
    'csrf_token':token
}
headers_info={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
response2=session1.post(url='http://47.107.178.45/phpwind/index.php',
                        params=url_params,
                        data=url_info,
                        headers=headers_info)
date=response2.json()
date_str=json.dumps(date)
print(date_str)
statu=re.findall('_statu=(.+?)"',date_str)[0]
print(statu)

url_params={
    'm':'u',
    'c':'login',
    'a':'welcome',
    '_statu':statu
}
response3=session1.get(url='http://47.107.178.45/phpwind/index.php',
                        params=url_params,
                        headers=headers_info)

url_params={
    'c':'thread',
    'fid':'81'
}

response4=session1.get(url='http://47.107.178.45/phpwind/index.php',
                       params=url_params)
#进入发帖界面
url_params={
    'c':'post',
    'fid':'81'
}
response5=session1.get(url='http://47.107.178.45/phpwind/index.php',
                       params=url_params)
#发帖
url_params={
    'c':'post',
    'a':'doadd',
    '_json':'1',
    'fid':'81'
}
#方式1
data={
    'atc_title':'axin9999',
    'atc_content':'fangqiba',
    'pid':'',
    'tid':'',
    'special':'default',
    'reply_notice':'1',
    'csrf_token':token
}
response6=session1.post(url='http://47.107.178.45/phpwind/index.php',
                       params=url_params,
                       data=data,
                       #headers=headers_info
                        )
#方式2
# form_data = OrderedDict(
#     [
#         ("atc_title",(None,'axin123')),
#        ("atc_content",(None,'123456')),
#         ("pid",(None,'')),
#         ("tid",(None,'')),
#         ("special",(None,'default')),
#         ("reply_notice",(None,'1')),
#         ("csrf_token",(None,token))
#     ]
# )
# response6=session1.post(url='http://47.107.178.45/phpwind/index.php',
#                        params=url_params,
#                        files=form_data,
#                        # headers=headers_info
#                         )

print(response6.content.decode('utf-8'))