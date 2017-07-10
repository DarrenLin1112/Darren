motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='Darren'
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('Amy')
print(motorcycles)

motorcycles=[]
motorcycles.append('Tiger')
motorcycles.append('Julia')
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(3,'ducati')
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
del motorcycles[0]
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


motorcycles=['Amy','Darren','Tiger']
last_owned=motorcycles.pop(1)
print('The last motorcycle I owned was a '+last_owned.title()+'.')
print(last_owned)


motorcycles=['Amy','Darren','Tiger']
print(motorcycles)
motorcycles.remove('Tiger')
print(motorcycles)

motorcycles=['Amy','Darren','tiger']
print(motorcycles)
too_expensive='tiger'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA '+too_expensive.title()+' is too expensive for me.')
