#From the sys package, open the "argument variables" feature.
from sys import argv

#Name the argument variables: script and filename
script, filename = argv

#Creates a variable called "txt", which job is to open the filename given when the user started the script; "python2.7 ex15.py ex15_sample.txt"
txt = open(filename)

#Prints the name of your file.
print "Here's your file %r:" % filename
#Reads the file you requested. Directly translated, it sounds like this; "ex15_sample.txt.read", which obviously means "Read the ex15_sample.txt file"
print txt.read()

#Closes the file. It's important to close files when you're done with them.
print txt.close()

#Prints the text "Type the filename again:"
print "Type the filename again:"
#Creates a new variable "file_again", and prompts the user to enter the filename again. The filename will be typed after the "> "
file_again = raw_input("> ")

#Creates another variable called "txt_again", which opens the file you entered in the previous command.
txt_again = open(file_again)

print txt_again.read()

#Closes the file. It's important to close files when you're done with them.
print txt_again.close()
