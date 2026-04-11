# class Parrot:
#     # class attributes
#     name = ""
#     age = 0
#     def Parrot():

# # create parrot1 as object

# parrot1 = Parrot()
# parrot1.name = "blue"
# parrot1.age = 10

# # create parrot2 as object
# parrot2 = Parrot()
# parrot2.name = "woo"
# parrot2.age = 15

# # access attributes
# print(f"{parrot1.name} is {parrot1.age} years old")
# print(f"{parrot2.name} is {parrot2.age} years old")



class Person:
    name = "Denis"
    age = 25
    location = "Kampala"
    occuption = "Farmer"
    contact = 753207890

    def Sing():
        return('This person sings nicley')
print(Person.Sing())

#create another object of class person
Person2 = Person()
Person2.name = 'John'
Person2.age = 27
Person2.contact = 75697607
Person2.location ="Jinja"
Person2.occuption = 'Mechanic'

print(Person2.name)

# class Animal:
#     animal_name = 'Dog'
#     animal_type = 'Mamal'
#     animal_color = 'Brown'
#     animal_size = 'Medium',
#     animal_skin_texture = 'fur'
#     animal_owner = 'Denis'
#     animal_location = 'Kampala'

#     def Sound():
#         return ('This animal barks')
# print(Animal.Sound())