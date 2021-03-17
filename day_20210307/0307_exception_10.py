import requests
a=[1,2,3]

try:
    print(a[5])
except IndexError as e:
    print('下标越界')
#IndexError这种系统自带异常 位于python内建命名空间中
# 所有异常都是Exceptin的子类

from requests.exceptions import RequestException,ConnectionError
# ConnectionError RequestException Exception
# 孙子类 继承 子类 继承 父类
try:
    response=requests.get('https://www.123kkkasdsad.com',verify=False)
    print(response.content.decode('utf-8'))
except ConnectionError as e: #就近匹配原则
    print('连接异常')
except RequestException as e: #书写规则：最小子类写在最上面
    print('request出错')
except Exception as e:
    print('系统出错')
