#Created the function called cheese_and_crackers. Inside the paranthesis, there are two parameters, cheese_count and boxes_of_crackers.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#Prints out the text inside "" and the parameter "cheese_count" which will be defined later in the 		script
	print "You have %d cheeses!" % cheese_count
	#Prints out the text inside "" and the parameter "boxes_of_crackers" which will be defined later in 		the script
	print "You have %d boxes of crackers!" % boxes_of_crackers
	#Prints out the text inside "".
	print "Man that's enough for a party!"
	#Prints out the text inside "".
	print "Get a blanket.\n"

#Prints out the text inside "".
print "We can just give the function numbers directly:"
#Defines the new paramteres for the function call "cheese_and_crackers". 20 in this case refers to "chese_count", while 30 refers to "boxes_of_crackers"
cheese_and_crackers(20, 30)


#Prints out the text inside "".
print "OR, we can use variables from our script:"
#Defines amount_of_cheese in the next function
amount_of_cheese = 10
#Defines amount_of_crackers in the next function
amount_of_crackers = 50

#New function where we take use of the previously defined parameters.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#Prints out the text inside "".
print "We can even do math inside too:"
#Defines the parameters inside cheese_and_crackers using math
cheese_and_crackers(10 +20, 5 + 6)


#Prints out the text inside "".
print "And we can combine the two, variables and math:"
#Defines even more parameters...
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def bitches_and_hoes(bitch_count, hoe_count):
	print "I have %d dead bitches in my van!" % bitch_count
	print "At home, there are %d dead hoes!" % hoe_count

bitches_and_hoes(10, 15)

print "\nI can also print it like this:\n"

car = 90
poop = 20

bitches_and_hoes(car + 10, poop + 123)
