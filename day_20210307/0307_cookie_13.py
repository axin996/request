import requests
#1通過直接傳cookie的方式
cookie_dict={'like':'apple'}
response=requests.get(url='http://47.107.178.45/phpwind/',
             cookies=cookie_dict)
#2通過請求頭部
header_info={
    'Cookie':'like=apple'
}
response2=requests.get(url='http://47.107.178.45/phpwind/',
             headers=header_info)
#3 session對象添加cookie
session=requests.session()
session.cookies['like']='apple'
session.cookies['sb']='you'
session.get(url='http://47.107.178.45/phpwind/')

