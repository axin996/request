import requests
import re  #python当中处理正则表达式的内置模块
#创建一个session对象 把各个接口联系起来
session=requests.session()

response1=session.get('http://47.107.178.45/phpwind/')
str01=response1.content.decode('utf-8')
#print(str01)
value=re.findall('name="csrf_token" value="(.+?)"/>',str01)[0]
print(value)
url_params={
    'm':'u',
    'c':'login',
    'a':'dologin'
}
url_info={
    'username':'test02',
    'password':'123456',
    'csrf_token':value
}
headers_info={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
response2=session.post(url='http://47.107.178.45/phpwind/index.php',
                        params=url_params,
                        data=url_info,
                        headers=headers_info)
#在requests中每个请求都是完全独立的 不互相传输缓存、cookie等信息
#在requests中的session对象是把网页中所有缓存联系起来的一个对象
print(response2.json())
#总结 以后要做登录态之后的操作 或者非独立请求能够完成的操作 都需要用到session对象