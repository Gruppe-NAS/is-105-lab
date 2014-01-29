#Opens the package called sys, and then imports the argv feature from the chosen package.
from sys import argv

#Defines the variable argv as script and filename.
script, filename = argv

#Prints out the text inside "" and adds the argv variable we created.
print "If you wish to read the file '%s'. press the RETURN key" % filename
#Prints out the text inside ""
print "If you wish to exit, press CTRL-D now."

#Outputs ">> " as a pause in the script. The script will continue once the user presses enter.
raw_input(">> ")

#Prints out the text inside "" and adds the argv variable we created.
print "Opening '%s'" % filename
#Creates a variable called "target" which opens the filename we defined when we started the script. In this case we typed; "python2.7 ex16.2.py ex16-test.txt" which puts the "script" definition as ex16.2, and the "filename" definition as ex16-test.txt
target = open(filename)

#Reads the file.
print target.read()

#Adds a linebreak
print "\n"
#Prints the text inside the ""
print "To close the file, press the RETURN key"

#Outputs ">> " as a pause in the script. The script will continue once the user presses enter.
raw_input (">> ")

#Closes the file
print target.close()
