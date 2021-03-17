import requests

response=requests.get(url='https://www.baidu.com',timeout=0.1)#浮点型 单位s

response1=requests.get(url='https://www.baidu.com',timeout=(0.1,0.2))#元组 连接超时 接收数据超时

response2=requests.get(url='https://www.baidu.com',timeout=None)#直到服务器返回数据为止