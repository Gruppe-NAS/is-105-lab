from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print "\nWhat is the first argument?\n",
first = raw_input()
print "What is the second argument?\n",
second = raw_input()
print "What is the third argument?\n",
third = raw_input()

print "\nThe first is %s, the second is %s, the third one is %s" % (first, second, third)
