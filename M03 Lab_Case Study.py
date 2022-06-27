'''
Yahya Alrobaie
File: M03 Lab_Case Study.py
June/26/2022
version 3.0
1. This app accept user input for a car.
2. The app will then ask the user for the year, make, model, doors, and type of roof and store thdata in the attributes above.
3.The app will then output the data in an easy-to-read and understandable format
'''

#vehicle class with constructor
class Vehicle:

	def __init__(self,kind):   #constructor for type
		self.kind = kind 

#subclass Automobile will inherit the attributes from Vehicle class
class Automobile(Vehicle):

	def __init__(self, kind , year , make , model , door ,roof):
		super().__init__(kind) #super function is called to  gets the definition of the parent class.
		self.year = year
		self.make = make
		self.model = model
		self.door = door
		self.roof = roof

# get the vehicle input from the user.
vehicle_kind=input("Enter the Type of vehicle(car, truck, plane, boat, ...):" + " ")
vehicle_year=input("Enter the year:" + " ")
vehicle_make=input("Enter the manufacture:" + " ")
vehicle_model=input("Enter the model:" + " ")
vehicle_door=input("Enter the number of doors(2 or 4):" + " ")
vehicle_roof=input("Enter the roof type(solid or sun roof):" + " ")

# Store all entered vehicle information
vehicle_information = Automobile(vehicle_kind , vehicle_year , vehicle_make , vehicle_model,  vehicle_door, vehicle_roof)

# to check my code
           # print(vehicle_information)


#print out the vehicle infromation
print("\n+++++++++++++++++++++++++++++++++++++++++++++++")
print("Vehicle Type:" + " " + vehicle_information.kind)
print("Year:" + " " + vehicle_information.year )
print("Make:" + " " + vehicle_information.make)
print("Model:" + " " + vehicle_information.model)
print("Number of doors:" + " " + vehicle_information.door)
print("Type of roof :" + " " + vehicle_information.roof)