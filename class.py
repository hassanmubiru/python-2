# class MyClass:
#     x = 5
# result = MyClass()
# print(result.x)


class Parrot:
    # class attribute
    name = ""
    age = 0

    # create parrot1 as object
    parrot1 = Parrot()
    parrot1.name = "blue"
    parrot1.age = 10

    # create parrot2 as object
    parrot2 = Parrot()
    parrot2.name = "woo"
    parrot2.age = 15

    # access attributes
    print(f"{parrot1.name} is {parrot1.age} year old")
    print(f"
