import requests
# 上传文件
#处理方式 简单处理
excel_file_obj=open('stu_info.xlsx','rb')
#excel_file_date={'file':excel_file_obj}

# 处理方式:显示的设置文件名、文件类型和请求头
excel_file_date={'file':('111.xlsx',excel_file_obj)}

response=requests.post(url='http://httpbin.org/post')
print(response.content.decode('utf-8'))