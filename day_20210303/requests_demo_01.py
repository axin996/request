import requests

# rp=requests.get('http://www.hnxmxit.com')
# print(rp.content.decode('utf-8'))

# https请求方式: GET https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
# 协议 https
# 主机地址 api.weixin.qq.com
# 接口地址 cgi-bin/token
# 参数 grant_type=client_credential&appid=APPID&secret=APPSECRET

#方式1
rs=requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxdc8562b5d4150019&secret=ecd278da52077dade43b50ad7c7ddeb6')
print(rs.content.decode('utf-8'))

#方式2
url_params={
    "grant_type":"client_credential",
    "appid":"wxdc8562b5d4150019",
    "secret":"ecd278da52077dade43b50ad7c7ddeb6"
}

rs1=requests.get(url='https://api.weixin.qq.com/cgi-bin/token',
                 params=url_params) # 这样请求可以是字典格式的url参数
print(rs1.content.decode('utf-8'))