fruits = ["apple","manago","pinapple","banana"] # list of string
# numbers = [10,20,30,40,50]
# mixed = ["Error",26,True] # list can mix types
# empty = []

# print(fruits[0])
# print(fruits[1])
# print(fruits[-1])
# print(fruits[-2])

# print(numbers[1:3])
# print(numbers[:2])
# print(numbers[2:])

fruits.append("oranges")
print(fruits)


fruits.insert(2,'Carrot')
print(fruits)

fruits.remove('Carrot')
print(fruits)

fruits.pop()
print(fruits)

print(len(fruits))

#in
print('apple' in fruits)
print('carrots' in fruits)

# sort
num2 = [3,2,4,5,6.7]
num2.sort()
print(num2)
