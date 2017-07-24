class Car():
	--snip--
	
	def update_odometer(self, mileage):
		--snip--
		
	def update_odometer(self, mileage):
		"""将里程表读数增加指定的量"""
		self.odometer_reading += miles
	
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

