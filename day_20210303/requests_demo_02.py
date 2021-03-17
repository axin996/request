import requests

head_info={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81"
}

# s = requests.session()
# s.keep_alive = False # 关闭多余连接
# s.get('https://www.baidu.com/s?wd=111',
#                       verify=False,
#                       headers=head_info) # 你需要的网址


response=requests.get(url='https://www.baidu.com/s?wd=111',
                      # verify=False,
                      headers=head_info)
print(response.content.decode('utf-8'))

