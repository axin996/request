import requests

url_params={
    "access_token" : "42_4-Ykh4LpNLI82ecRrqOE6tgwOCRDT1MBy1BPUVIRhhjYmGKZpgYPrI1BBw9a0bPL4mzmYa6nH31aiOSD2bRdAZXQAlCK-oa8gRkRHX0oA3FftVTf0spO65X_tMiMacS3k5em70kCsfihPeU0JXUdABAUIF"
}

tag_info={
    "tag":{"name":"newdreamP5P7"}
}

wx=requests.post(url='https://api.weixin.qq.com/cgi-bin/tags/create',
              params=url_params,
              json=tag_info)

print(wx.content.decode('utf-8'))