import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

auth=('API_V1','123456')
header_info1={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
             'Cookie':'user=912551a9-2397-11e9-94e4-005056ab5a7e; refresh_token=0d36f457-7342-45e2-a323-e86df0990933; '
                      'access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbmlkIjoiYWRtaW4iLCJybmQiOiIyNzI1NTEiLCJleHAiOjE2MTUzNjg0MTAsImFjY291bnQiOiI5MTI1NTFhOS0yMzk3LTExZTktOTRlNC0wMDUwNTZhYjVhN2UiLCJ1c2VybmFtZSI6IjkxMjU1MWE5LTIzOTctMTFlOS05NGU0LTAwNTA1NmFiNWE3ZSJ9.RHWr9WZP7_mi0IEo62w23FrcPuEGU6BWJgVL_T7YMkY; '
                      'account=912551a9-2397-11e9-94e4-005056ab5a7e; loginid=admin; connect.sid=s%3A0kXkFALOD40RnFKssvAVi0uSXhNW_dC3.vK46R%2BR%2BUVJf2Qpb%2BwIz7%2B%2B1l4rXi5jmSilDJP8q%2FTc'}

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
response1=requests.get('https://petest.gds-services.com/api/duties/get_staffs',
                       verify = False,
                       headers=header_info1,
                       #auth=auth,
                       )

print(response1.status_code)
print(response1.content.decode('utf-8'))
print(response1.headers)
print('===============')


header_info2={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
             'Cookie':'user=912551a9-2397-11e9-94e4-005056ab5a7e; refresh_token=0d36f457-7342-45e2-a323-e86df0990933; '
                      'access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbmlkIjoiYWRtaW4iLCJybmQiOiIyNzI1NTEiLCJleHAiOjE2MTUzNjg0MTAsImFjY291bnQiOiI5MTI1NTFhOS0yMzk3LTExZTktOTRlNC0wMDUwNTZhYjVhN2UiLCJ1c2VybmFtZSI6IjkxMjU1MWE5LTIzOTctMTFlOS05NGU0LTAwNTA1NmFiNWE3ZSJ9.RHWr9WZP7_mi0IEo62w23FrcPuEGU6BWJgVL_T7YMkY; '
                      'account=912551a9-2397-11e9-94e4-005056ab5a7e; loginid=admin; connect.sid=s%3A0kXkFALOD40RnFKssvAVi0uSXhNW_dC3.vK46R%2BR%2BUVJf2Qpb%2BwIz7%2B%2B1l4rXi5jmSilDJP8q%2FTc',
              'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbmlkIjoiYWRtaW4iLCJybmQiOiIyNzI1NTEiLCJleHAiOjE2MTUzNjg0MTAsImFjY291bnQiOiI5MTI1NTFhOS0yMzk3LTExZTktOTRlNC0wMDUwNTZhYjVhN2UiLCJ1c2VybmFtZSI6IjkxMjU1MWE5LTIzOTctMTFlOS05NGU0LTAwNTA1NmFiNWE3ZSJ9.RHWr9WZP7_mi0IEo62w23FrcPuEGU6BWJgVL_T7YMkY',
              'Content-Type': 'application/json;charset=utf-8',
              }

response2=requests.post('https://petest.gds-services.com/api/notice/sms/send',
                       verify = False,
                       headers=header_info2,
                       auth=auth,
                       )

print(response2.status_code)
print(response2.content.decode('utf-8'))
print(response2.headers)
print('===============')

header_info3={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
             'Cookie':'user=912551a9-2397-11e9-94e4-005056ab5a7e; refresh_token=0d36f457-7342-45e2-a323-e86df0990933; '
                      'access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbmlkIjoiYWRtaW4iLCJybmQiOiIyNzI1NTEiLCJleHAiOjE2MTUzNjg0MTAsImFjY291bnQiOiI5MTI1NTFhOS0yMzk3LTExZTktOTRlNC0wMDUwNTZhYjVhN2UiLCJ1c2VybmFtZSI6IjkxMjU1MWE5LTIzOTctMTFlOS05NGU0LTAwNTA1NmFiNWE3ZSJ9.RHWr9WZP7_mi0IEo62w23FrcPuEGU6BWJgVL_T7YMkY; '
                      'account=912551a9-2397-11e9-94e4-005056ab5a7e; loginid=admin; connect.sid=s%3A0kXkFALOD40RnFKssvAVi0uSXhNW_dC3.vK46R%2BR%2BUVJf2Qpb%2BwIz7%2B%2B1l4rXi5jmSilDJP8q%2FTc',
              'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbmlkIjoiYWRtaW4iLCJybmQiOiIyNzI1NTEiLCJleHAiOjE2MTUzNjg0MTAsImFjY291bnQiOiI5MTI1NTFhOS0yMzk3LTExZTktOTRlNC0wMDUwNTZhYjVhN2UiLCJ1c2VybmFtZSI6IjkxMjU1MWE5LTIzOTctMTFlOS05NGU0LTAwNTA1NmFiNWE3ZSJ9.RHWr9WZP7_mi0IEo62w23FrcPuEGU6BWJgVL_T7YMkY',
              'Content-Type': 'application/json;charset=utf-8',
              }

response3=requests.post('https://petest.gds-services.com/api/files/show_file',
                       verify = False,
                       headers=header_info3,
                       auth=auth,
                       )

print(response3.status_code)
print(response3.content.decode('utf-8'))
print(response3.headers)
print('===============')

