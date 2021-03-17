import requests
#重定向 请求返回3** request默认支持重定向
response=requests.get('http://www.360buy.com',allow_redirects=False)
print(response.content.decode('utf-8'))
print(response.url)
print(response.history)

