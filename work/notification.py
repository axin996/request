import requests

params={
    'category': 'alarm',
    'to': '1004926490@qq.com',
    'subject': '123',
    'content': '321'
}

auth=('API_V1','123456')

response=requests.post('http://192.168.242.165:8080/mail/submit',
                       params=params,)
                       #verify = False,
                       #auth=auth)

print(response.content.decode('utf-8'))