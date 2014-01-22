# Definition of the variable "x"
x = "There are %d types of people." % 10
# Definition of the variable "binary"
binary = "binary"
# Definition of the variable "do_not"
do_not = "don't"
# Definition of the variable "y"
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints variable "x"
print x
# Prints variable "y"
print y

# Prints the text inside "" + the text inside variable "x"
print "I said: %r." % x
# Prints the text inside "" + the text inside variable "y"
print "I also said: '%s'." % y

# Definition of the variable "hilarious"
hilarious = False
# Definition of the variable "joke_evaluation"
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints the variable "joke_evaluation" with the variable "hilarious where the %r is.
print joke_evaluation % hilarious

# Definition of the variable "w"
w = "This is the left side of..."
# Definition of the variable "e"
e = "a string with a right side."

# Prints the variable "w" + the variable "e"
print w + e
