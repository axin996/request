import requests
# 响应行 响应头  响应正文
response=requests.get(url='http://www.hnxmxit.com')
print(response.status_code) # 响应状态码
print('==========')
print(response.reason) # 响应信息 ok
print('==========')
print(response.headers.get('Content-Type'))
print('==========')
print(response.url)
print('==========')
print(response.cookies)
print('==========')
print(response.encoding) # 获取响应的编码格式
print('==========')

#响应正文的四种获取方式
# 1、响应内容文本
print(response.text)
print('==========')
# 2、二进制响应内容
print(response.content)
print('==========')
# 响应正文为图片
from PIL import Image
from io import BytesIO
response_img=requests.get(url='https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E6%81%B6%E9%AD%94&step_word=&hs=0&pn=5&spn=0&di=7700&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=1688250228%2C4186624614&os=3644172914%2C3463975212&simid=45392872%2C531015956&adpicid=0&lpn=0&ln=1710&fr=&fmq=1615086279091_R&fm=result&ic=&s=undefined&hd=&latest=&copyright=&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%3A%2F%2Fimg9.51tietu.net%2Fpic%2F2019-091222%2Fktxuerbedi4ktxuerbedi4.jpg%26refer%3Dhttp%3A%2F%2Fimg9.51tietu.net%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Djpeg%3Fsec%3D1617678283%26t%3D6b8cc93bd881daa5cc8ae340cd56ce95&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bc8ptjp7_z%26e3BgjpAzdH3F15g24wgAzdH3Fnm9l0c_z%26e3Bip4s&gsm=6&rpstart=0&rpnum=0&islist=&querylist=&force=undefined')
img_obj=Image.open(response_img,'rb')
