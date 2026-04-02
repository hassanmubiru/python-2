thisdict ={
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    # "colors" : ["red","blue","green"]

}
# print(type(thisdict))
# print(len(thisdict))
# thisdict.update({'colors':'yellow'})
# thisdict.pop("brand")
# thisdict.popitem()
# print(thisdict)


# students = [
#     {"name":"Alice","score":90},
#     {"name":"Bob","score":60},
#     {"name":"denis","score":98}
# ]

# for s in students:
#     if s["score"] >= 80:
#         print(s["name"],"passed")

# # 

# employees = [
#     {"name": "Hassan","age":30},
#     {"name": "Denis","age":25}
# ]

# employees = [{"name": f"person{i+1}","age":20 + i} for i in range(3)]
# print(employees[0])
# print(employees[1]['name'])


# a = [{'name': 'Error',"age":25},{'name':'denis','age':30}]
# print(a)
# print(type(a))

# a = []

# for i in range(3):
#     a.append({"name": f"person {i+1}","age" : 20 +i})
# print(a)

# name =["Denis","Bash","error"]
# age = [25,30,40]

# x = [{"name": name[i],"age":age[i]} for i in range(len(name))]
# # print(x)

# text = "hello,world"

# print(text.strip())
# print(text.replace('fun','asesome'))
# print(text.upper())

# words = 'apple banana mango'.split()
# print(words)
# print(','.join(words))

# name  = 'Denis'
# # print(f'hello,{name.upper()}')

# # text = 'Welcome to python for beginers'
# # print(f'result :{text.strip().upper()}')
# print(f'result : {name.strip().upper()}')

# user = 'Denis'
# print(f'{user=}')

# def get_status(score):
#     return "Pass" if score >= 50 else "Fail"
# score = 30
# print(f"Your score is : {get_status(score)}")

first_name = 'Jane'
last_name = 'error'

print(f'FullName : {first_name} {last_name}')