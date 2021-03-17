import requests
#代理用途1.爬虫限制ip 多个代理去抓取数据 2.境外项目 连接vpn测试
#连接svn有用户名密度的话'http':'http://user：passname@127.0.0.1:8888'
proxy_server={
    'http':'http://127.0.0.1:8888',
    'https':'https://127.0.0.1:8888'
}
response=requests.get(url='http://www.hnxmxit.com',
                      proxies=proxy_server)
#要开代理服务器 才可以 这里用的是青花瓷的
print(response.status_code)