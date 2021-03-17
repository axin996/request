import requests
import jsonpath
import json
response=requests.get(' https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxdc8562b5d4150019&secret=ecd278da52077dade43b50ad7c7ddeb6')
json_date=response.json()
access_token=jsonpath.jsonpath(json_date,'$.access_token')
print(access_token)
#创建标签
url_params={'access_token':access_token}
data_params={
    'tag':{'name':'大学生组6'}
}
data_json_params=json.dumps(data_params,ensure_ascii=False)
response2=requests.post(url='https://api.weixin.qq.com/cgi-bin/tags/create',
                        params=url_params,
                        data=data_json_params.encode('utf-8'))
print(response2.json())
#删除标签
jsdate=response2.json()
bqid=jsonpath.jsonpath(jsdate,'$.tag.id')[0]
print(bqid)
data_params2={   "tag":{        "id" : bqid   } }
data_json_params2=json.dumps(data_params2)
response3=requests.post(url='https://api.weixin.qq.com/cgi-bin/tags/delete',
                        params=url_params,
                        data=data_json_params2
                        )
print(response3.json())