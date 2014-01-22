# A variable called "cars", which is equal to 100
cars = 100

# A variable called "space_in_a_car", which is equal to 4
space_in_a_car = 4.0

# A variable called "drivers", which is equal to 30
drivers = 30

# A variable called "passengers", which is equal to 90
passengers = 90

# A variable called "cars_not_driven", which is equal to the variable "cars" - "drivers" which is 70
cars_not_driven = cars - drivers

# A variable called "cars_driven", which is equal to the variable "drivers" which is 30
cars_driven = drivers

# A variable called "carpool_capacity", which is equal to "cars_driven" multiplied by "space_in_a_car" which is 120
carpool_capacity = cars_driven * space_in_a_car

# A variable called "average_passengers_per_car", which is equal to "passengers" divided by "cars_driven" which is 3
average_passengers_per_car = passengers / cars_driven


# Prints "There are 100 cars available."
print "There are", cars, "cars available."

# Prints "There are only 30 drivers available."
print "There are only", drivers, "drivers available."

# Prints "There will be 70 empty cars today."
print "There will be", cars_not_driven, "empty cars today."

# Prints "We can transport 120 people today."
print "We can transport", carpool_capacity, "people today."

# Prints "We have 90 to carpool today."
print "We have", passengers, "to carpool today."

# Prints "We need to put about 3 in each car."
print "We need to put about", average_passengers_per_car, "in each car."
