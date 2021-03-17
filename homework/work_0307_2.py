import requests
import re
import random
host='47.107.178.45'
session1=requests.session()
url_value={
    'm':'u',
    'c':'register'
}
response1=session1.get(url='http://%s/phpwind/index.php'%host,
                       params=url_value)
response1_date=response1.content.decode('utf-8')
#print(response1_date)
token=re.findall('name="csrf_token" value="(.+?)"/>',response1_date)[0]
print(token)
print('+++++++++++++++++++++++++++++')
url_value2={
    'm':'u',
    'c':'register',
    'a':'checkusername'
}
num=str(random.randint(1000,9999))
data_value={
    'csrf_token':token,
    'username':'axin%s'%num
}
response2=session1.post(url='http://%s/phpwind/index.php'%host,
                        params=url_value2,
                        data=data_value)
print(response2.content.decode('utf-8'))
