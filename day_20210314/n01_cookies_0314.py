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

session1.cookies.set('_ac_app_ua','c0c9dc4075ac297b74')
session1.cookies.set('csrf_token',token)
session1.cookies.set('zFb_lastvisit','2465%091615683068%09%2Fphpwind%2Findex.php%3Fm%3Du%26c%3Dlogin%26a%3Dwelcome%26_statu%3Dd2lFS0tyeUtoZnd0Sk5rTmxXU0k5RVU3SHJpYlc0WEFJOFl5S1J1OGYlMkI0MXJzYm43TnBJTXVRMXluTm5iTThIbXo3ZFVRJTNEJTNEfGh0dHA6Ly80Ny4xMDcuMTc4LjQ1L3BocHdpbmQvfA')
session1.cookies.set('zFb_winduser','AWrHUshN2Dr8le140KHR8X0az3FyZBKd7u1n4jbuP9v90Y4Dhh5evW2pffY%3D')
session1.cookies.set('zFb_visitor','pjibP%2B1P4qoKpY3mEzEQAe1bbX8Mfp5Ces1cUBVwXG64OD91')

# uudid	cms13857129-fa42-3231-76af-90272a83ea5e
# radius	115.172.82.23


#发帖
url_params={
    'c':'post',
    'a':'doadd',
    '_json':'1',
    'fid':'81'
}

# data={
#     'atc_title':'axin9999',
#     'atc_content':'fangqiba',
#     'pid':'',
#     'tid':'',
#     'special':'default',
#     'reply_notice':'1',
#     'csrf_token':token
# }
# response6=session1.get(url='http://47.107.178.45/phpwind/index.php',
#                        params=url_params,
#                        data=data,
#                        )

form_data = OrderedDict(
    [
        ("atc_title",(None,'axin996')),
       ("atc_content",(None,'123456')),
        ("pid",(None,'')),
        ("tid",(None,'')),
        ("special",(None,'default')),
        ("reply_notice",(None,'1')),
        ("csrf_token",(None,token))
    ]
)
response6=session1.post(url='http://47.107.178.45/phpwind/index.php',
                       params=url_params,
                       files=form_data,
                       )

print(response6.content.decode('utf-8'))