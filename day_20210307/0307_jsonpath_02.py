import jsonpath

json_obj={"name":"小孩","age":14}
print(json_obj['name'])
print(jsonpath.jsonpath(json_obj,'$.name')[0])