import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
headers={
    'Cookies':'account=912572d8-2397-11e9-94e4-005056ab5a7e; loginid=chaiguangfei; connect.sid=s%3A03KSDd-7ZMYKOoIlCWUqdKVUWg2tbxbY.nuHHrVTsuu5WK8k2VjHJM%2F8sv1U9KsFVNgg%2BptwuuP4; access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbmlkIjoiYWRtaW4iLCJybmQiOiI3NzgxNDgiLCJleHAiOjE2MTUzNDg0NjYsImFjY291bnQiOiI5MTI1NTFhOS0yMzk3LTExZTktOTRlNC0wMDUwNTZhYjVhN2UiLCJ1c2VybmFtZSI6IjkxMjU1MWE5LTIzOTctMTFlOS05NGU0LTAwNTA1NmFiNWE3ZSJ9.XN8g64UCGNMnKmRcHC7oGQtFoX76bkoOWsaokUy9QJk; refresh_token=a208bfda-39b6-4ae9-85d9-aa973df74757; user=912551a9-2397-11e9-94e4-005056ab5a7e',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'Authorization':'',
    'Accept': 'application/json, text/plain, */*'
}
#auth=('API_V1','123456')
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
response=requests.get(url='https://petest.gds-services.com/api/cbms/get_dcs?user=912551a9-2397-11e9-94e4-005056ab5a7e',
                      verify=False,
                      headers=headers,)
                      #auth=auth)
print(response.content.decode('utf-8'))
print(response.headers)
