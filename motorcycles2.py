message = ['honda','yamaha','suzuki']
print(message)

message[2]="darren"
print(message)

message = ['honda','yamaha','suzuki']
message.append('ducati')
print(message)

message = ['honda','yamaha','suzuki']
del message[0]
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

poppeding_motorcycle = motorcycles.pop()
print(motorcycles)
print(poppeding_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
print(motorcycles)

for value in range(1,11):
	print(value)

message = list(range(2,11))
print(message)

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)
