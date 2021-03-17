import requests
# 去除警告
requests.packages.urllib3.disable_warnings()
# 打开青花瓷 需要证书  可以选择忽略证书 verify=False
response=requests.get('https://www.baidu.com',verify=False)
print(response.content.decode('utf-8'))

# 下载证书 找开发要 当前网站可以自己下载证书
# response1=requests.get('https://www.12306.cn',cert=('/path/server.crt','/path/key')) # 加上证书的地址
