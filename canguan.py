class Restaurant():
	"""创建一个名为Restaurant 的类"""

	def __init__(self,restaurant_name,cuisine_type):
		"""初始属性restaurant_name和cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.odometer_reading = 0
	
	def describe_restaurant(self):
		print(self.restaurant_name.title()+" The restaurant is open")
		
	def open_restaurant(self):
		print(self.cuisine_type.title()+" The restaurant is open")

restaurant = Restaurant('darren','amy')

print("This restaurant " + restaurant.restaurant_name.title() + ".")
print("This restaurant " + restaurant.cuisine_type.title() + ".")

restaurant = Restaurant('willie',6)

print("\nMy dog's name is " + restaurant.restaurant_name.title() + ".")
print("My dog is " + str(restaurant.cuisine_type) + " years old.")


class User():
	"""创建一个名为User 的类"""
	
	def __init__(self,first_name,last_name):
		"""初始属性first_name和last_name"""
		self.first_name = first_name 
		self.last_name = last_name
		self.odometer_reading = 0
		
	def describe_user(self):
		"""定义一个名为describe_user()的方法"""
		print(self.first_name.title() + " is my first name")
		
	def greet_user(self):
		"""定义一个名为greet_user()的方法"""
		print(self.last_name.title() + " is my last name")
		
	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
message = User('darren','lin')

print("\nMy first name is " + message.first_name.title() + ".")
print("My last name is " + message.last_name.title() + ".")

bibiname = User('amy','lin')
kikiname = User('kiki','zhang')

print("\nYour first name is " + bibiname.first_name.title() + ".")
print("Your last name is " + bibiname.last_name.title() + ".")

print("\nYour first name is " + kikiname.first_name.title() + ".")
print("Your last name is " + kikiname.last_name.title() + ".")

	def update_odometer(self,mileage):
		"""将里程表读数设置为指定的值"""
		self.odometer_reading = mileage
		
message.update_odometer(23)
message.read_odometer()
