class Car():
	"""一次模拟汽车的简单尝试"""
	
	def __init__(self, make, model, year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def message(self):
		"""返回整洁的描述性信息"""
		long_name = str(self.year)+ ' ' +self.make + ' ' +self.model
		return long_name.title()
	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
my_new_car = Car('BMW','520li','2017')
print(my_new_car.message())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()



