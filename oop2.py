# class MyClass:
#     x = 5
# result = MyClass()
# print(result.x)


# class Parrot:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# parrot1 = Parrot("blu",10)
# parrot2 = Parrot("woo",15)
# print(f"{parrot1.name} is {parrot1.age} years old")
# print(f"{parrot2.name} is {parrot2.age} years old")


class BankAccount:
    def __init__(self,owner,balance = 0):
        self.owner = "Denis"
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited :${amount:.2f} .New balance: ${self.balance:.2f}")
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
        print(f"withdraw ${amount:.2f}. New balance: ${self.balance:.2f}")
    def get_balance(self):
        return f"${self.balance:.2f}"
    
# using class

acc = BankAccount("denis",500)
acc.deposit(200)
acc.withdraw(100)
acc.withdraw(700)
print(acc.get_balance())