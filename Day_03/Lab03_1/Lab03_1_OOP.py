######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.01
# Topic: Lab03_1 Python OOP Lab with 6 questions
######################################################

#Parent class vehicle
class vehicle:

	#instance (object) attributes
	def __init__(self, name, max_speed, milage):
		self.name = name
		self.max_speed= max_speed
		self.milage = milage

	
	def seating_capacity(self, capacity):
	
		fstring = f"The seating capacity of a {self.name} is {capacity} passengers"
		return fstring
		
#Child class bus
class bus(vehicle):

	#instance (object) attributes
	def __init__(self, name, max_speed, milage, capacity=50):
		super().__init__(name, max_speed, milage)
		self.capacity = capacity
		
		
	def seating_capacity(self, capacity=50):
		fstring = f"The seating capacity of a {self.name} is {capacity} passengers"
		return fstring
	
	def fare(self):
		busFare = self.capacity * 100
		return busFare
		
		
		
