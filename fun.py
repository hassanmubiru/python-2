# def greet():
#     print('Hello world')
# # call the function
# greet()

# print('outside function')

# def greet(name):
#     print('Hello',name)

# greet('Denis')
# greet('Error')

# def add_numbers(num1,num2):
#     sum = num1 + num2
#     print('sum :',sum)

# add_numbers(10,30)

# def find_square(num):
#     result = num * num
#     return result
# square = find_square(3)
# print('Square :',square)

# import math

# # square_root = math.sqrt(4)
# # print('Square Root of 4 is',square_root)

# # #pow() comptes the power
# # power = pow(2,3) 

# # print('2 to power 3 is',power) 


# def is_adult(age):
#     if age >= 18:
#         return True
#     else:
#         return False
# print(is_adult(20))
# print(is_adult(15))

# def greet(name,greeting='Hello'):
#     print(greeting +","+ name +"!")
# greet("Denis")
# greet('Hassan','Good Evening')


def calculate_total(price,quantity,discount=0):
    subtotal = price * quantity
    total = subtotal - discount
    return total

print(calculate_total(10,3))
print(calculate_total(10,3,5))
print(calculate_total(50,2,0))