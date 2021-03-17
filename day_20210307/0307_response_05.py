import requests
#解决乱码
response=requests.get(url='https://www.baidu.com')
#方式1
print(response.encoding) #ISO-8859-1
print(response.headers)# 'Content-Encoding': 'gzip'
# 由于没有Content-Type表明格式 requests 通过头部信息 Content-Encoding进行正文编码的推测 g-zip==>ISO-8859-1  导致乱码
response.encoding = 'utf-8'
print(response.text)
#方式2
print(response.apparent_encoding) # 根据网页正文预测编码格式
response.encoding = response.apparent_encoding # 自动解决响应乱码问题
print(response.text)