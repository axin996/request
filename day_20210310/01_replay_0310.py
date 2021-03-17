import requests
import re
import json
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
print(response3.content.decode('utf-8'))