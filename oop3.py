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