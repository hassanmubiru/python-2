class Car:
    def __init__(self,brand,model,year,mileage=0):
        self.brand = brand
        self.model = model
        self.year  = year
        self.mileage = mileage

    def drive(self,distance):
        self.mileage += distance
        print(f"Drove {distance} km. Total mileage: {self.mileage} km")
    
    def get_info(self):
        return f"{self.year}{self.brand} {self.model},Mileage :{self.mileage} km"
    

#Using the class
my_car = Car("Toyota","Carolla",2021,15000)
print(my_car.get_info())


my_car.drive(120)
my_car.drive(80)

print(my_car.get_info())

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity,mileage=0):
        super().__init__(brand, model, year, mileage)
        self.battery_capacity = battery_capacity
        self.battery_level = battery_capacity

    def drive(self,distance):
        energy_used =distance * 0.2 #assume 0.2 kwh per km
        if energy_used > self.battery_level:
            print(f"Not enough battery to drive that far !")
        else:
            self.battery_level -= energy_used
            super().drive(distance)

    def charge(self,amount):
        self.battery_level = min(self.battery_capacity,self.battery_level + amount)
        print(f"Charged battery. Current level: {self.battery_level:1f} kwh")
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info},Battery: {self.battery_level:1f}/{self.battery_capacity} kwh"

#using the classes
my_tesla = ElectricCar("Tesla","Model 3",2022,battery_capacity=75)
print(my_tesla.get_info())

my_tesla.drive(100)
my_tesla.drive(300)
my_tesla.drive(60)

print(my_tesla.get_info())