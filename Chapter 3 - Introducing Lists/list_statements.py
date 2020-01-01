# create a list
motorcycles = []
print(motorcycles)
print("list contains no values")

# append statement
motorcycles.append('honda')
print(f"\nmotorcycle {motorcycles[0]} has been appended to the list")
print(motorcycles)

# insert statement
motorcycles.insert(0, 'suzuki')
print(f"\nmotorcycle {motorcycles[0]} has been added inserted at index position 0")
print(motorcycles)

# delete statement
del motorcycles[0]
# print list
print(f"\nmotorcycle at index 0 has been removed")
print(motorcycles)

# pop method from end of list
motorcycles.append('suzuki')
print(f"\nmotorcycle {motorcycles[1]} has been added")
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(f"motorcycle {popped_motorcycles} has been popped from list")
print(motorcycles)

# pop method from any position
motorcycles.append('suzuki')
print(f"\nmotorcycle {motorcycles[1]} has been added")
print(motorcycles)
first_motorcycle = motorcycles.pop(0)
print(f"motorcycle {first_motorcycle} has been popped from list position 0")
print(motorcycles)

# remove method
motorcycles.append('suzuki')
motorcycles.append('ducati')
motorcycles.append('harley')
print(f"\n{motorcycles}")
motorcycles.remove('ducati')
print(motorcycles)
print("Ducati removed from list using removed() method")

print(f"\n{motorcycles}")
too_cheap = 'suzuki'
motorcycles.remove(too_cheap)
print(f"{too_cheap} has been removed from list and stored as too_cheap variable")
print(f"too cheap = {too_cheap.title()}")
print(motorcycles)
