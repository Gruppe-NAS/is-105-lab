inches = 2.54
pounds = 0.45
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d centimeters tall." % (height * inches)
print "He's %d kilos heavy." % (weight * pounds)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %r." % (
	age, (height * inches), (weight * pounds), age + (height * inches) + (weight * pounds))
