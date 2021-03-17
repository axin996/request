import requests

session = requests.session()

session.cookies.set(".CNBlogsCookie","8B81F97787EC6B722E57258167F23C9A0BC39CA98DC5191FD3BDD5D7BAF1420505B929538A7DD6E8DB343A9879229FA52E120F6E0F1024DA302E8C77C3AC8A5851EE76AE9FF592D189D9C5F4CF5AA1E31E1E7BBF",domain=".cnblogs.com",path="/")
session.cookies.set(".Cnblogs.AspNetCore.Cookies","CfDJ8EklyHYHyB5Oj4onWtxTnxaQJBL2Xan4sSj4XUNJWULWA5dMx_H4Qs4Q-MGuwMfn57TQSe-ewEFNPoAozw6r9RIV9qzjL4q2juiB43lQnz-LykaKpKuDmjcfDm1WvmHDNiS5AKZh6sEz2EYyThgIH1VekDvHDg3mYvIVrr5I5VpSJrC4KD4R32SOL58xpqXT3vgzDxaUIeBJE0pQZZTbirYxZgX580abDb0Scfv92euO60kAj4EpLqZZ5J9bTR8e95exhioSIjArqOkQAniOUJDYkrQjMvLtn2z4x_un5s7CMbFNhNppWTbjhGMujnWZgeG-ok3wAa-a3gJXyoc19_g9lPs2M1uPk4w5w_jQDvfDuVIxCp0o5fDyHHwvA9ikjZKNqrMkCPKi0lGECOLVLpX_g5ag0hvpYIzJ2L3r-bS6ykJ-QTRPNwd42CYWsPrszOEscBzusqrz-T1k8JUWtrKC5bz7rPYnxplMD2838daIHIil2p6cVHrB12HppkH_wML0xtFPjEWldFkkm2z85u4IwHiuzCZshjSGMtXZbe5P3EeGIhGNQOg0_ttrdBaFUw",domain=".cnblogs.com",path="/")
session.cookies.set(".AspNetCore.Antiforgery.b8-pDmTq1XM","CfDJ8EklyHYHyB5Oj4onWtxTnxYYnREVkopAA22KsPR9_ui-YuH3Rq8fw5xjVE5epkK6Q4OBFAoYkHVtxy1JUi5tOI6o1xG05ifRuBZmyaQLhbPF1KL55nNcpWVSQwLXCP2DB1CnAm5YztAjqgJ4lW6OZcs",domain="www.cnblogs.com",path="/")
session.cookies.set("__gads","ID=e62061ef6e4fd500-2216bed347c500cf:T=1608707472:S=ALNI_MZ5LKECUYr3xJ2hF_swQVV7mB6ItQ",domain=".cnblogs.com",path="/")
session.cookies.set('_ga','GA1.2.246923018.1599716076')
session.cookies.set('_gid','GA1.2.107886111.1615883287')
header_info={
    "content-type":"application/json; charset=UTF-8",
    "accept":"application/json, text/javascript, */*; q=0.01",
    "x-requested-with":"XMLHttpRequest",
    "requestverificationtoken":"CfDJ8EklyHYHyB5Oj4onWtxTnxZCcYIYzsDNiE718OUtV5vfDLLVx6azCxDMZmMPqwrFoafvSSxGYuAzdxqP3abQuz7sMzpGfL0q9Ox-jvwNpK_FCP50QGonLS684E2MfbxA9e-DHXW5WavWLaXN1o4Youz4h56xWJGeH01uUR499InR40NM3NLpqaZ3u62fn6TGjg",
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

post_data = {
	"postId": 14544714,
	"body": "期待后续更新",
	"parentCommentId": 0
}

response = session.post(url='https://www.cnblogs.com/GuZhenYin/ajax/PostComment/Add.aspx',
                        headers = header_info,
                        json=post_data,
                        verify=False
                        )
print( response.content.decode('utf-8') )