import json

my_data = """arg1,arg2,arg3,arg4,arg5,arg6
this,is,a,comma,separated,string
this,is,a,comma,separated,string
""".split("\n")

test_join = ", ".join(my_data)
print(test_join)

my_data.pop()


headers = my_data.pop(0).split(",")

list_of_dicts = []

for data in my_data:
    new_dict_element = {}
    new_entry = data.split(",")

    for i, header in enumerate(headers):
        new_dict_element[header] = new_entry[i]

    list_of_dicts.append(new_dict_element)

print(list_of_dicts)


with open("data.json", "w", encoding="utf-8") as f:
    json.dump(list_of_dicts, f, ensure_ascii=False, indent=4)
