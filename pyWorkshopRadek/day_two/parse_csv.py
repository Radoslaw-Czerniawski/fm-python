import json

my_data = """arg1,arg2,arg3,arg4,arg5,arg6
this,is,a,comma,separated,string
this,is,a,comma,separated,string
""".split("\n")

my_data.pop()

headers = my_data.pop(0).split(",")

my_data = [data.split(",") for data in my_data]

list_of_dicts = [dict(zip(headers, val)) for val in my_data]

print(list_of_dicts)
