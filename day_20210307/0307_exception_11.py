import requests
from requests.exceptions import RequestException,ConnectTimeout
try:
    response=requests.get('https://www.baidu.com',timeout=0.01)
    print(response.content.decode('utf-8'))
except ConnectTimeout as e:
    print('10ms内不能返回')
except RequestException as e:
    print(e)