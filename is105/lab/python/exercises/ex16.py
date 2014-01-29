#Opens the sys package, and initiates the argv feature in this package.
from sys import argv

#Defines the argv as script and filename.
script, filename = argv

#Prints the text inside the "" and adds the filename you gave when you initiated the command.
print "We're going to erase %r." % filename
#Prints the text inside the ""
print "If you don't want that, hit CTRL-C (^C)."
#Prints the text inside the ""
print "If you do want that, hit RETURN."

#Outputs a questionmark, which will act as a hold command for the script, either until the user presses "CTRL-D", which is the keybind for exiting a command, or RETURN, which will continue the script.
raw_input("?")

#Prints the text inside ""
print "Opening the file..."
#Creates a variable called "target". The variable opens the filename which we defined when we initiated the script. The 'w' means we open the file in write mode.
target = open(filename, 'w')

#Prints the text inside ""
print "Truncating the file. Goodbye!"
#The target variable (the file we chose) is truncated (deleted). This is not nessecary since we have already opened the file in write mode.
target.truncate()

#Prints the text inside ""
print "Now I'm going to ask you for three lines."

#Creates a variable called "line1", which requires the user to input some data.
line1 = raw_input("line 1: ")
#Creates a variable called "line2", which requires the user to input some data.
line2 = raw_input("line 2: ")
#Creates a variable called "line3", which requires the user to input some data.
line3 = raw_input("line 3: ")

#Prints the text inside ""
print "I'm going to write these to the file."

#Replaced all the target.write lines with this single one. Basically it cuts 6 lines of code down to 1. Here, we take use of the %s and \n to call to each variable within the paranthesis; line1, line2, line3.
target.write("%s\n%s\n%s\n" %(line1, line2, line3))


#Writes the "line1" data which we specified when we created the variable in to the now empty file (target).
#target.write(line1)
#Writes a linebreak in the file.
#target.write("\n")
#Writes the "line2" data which we specified when we created the variable in to the now empty file (target).
#target.write(line2)
#Writes a linebreak in the file.
#target.write("\n")
#Writes the "line3" data which we specified when we created the variable in to the now empty file (target).
#target.write(line3)
#Writes a linebreak in the file.
#target.write("\n")


#Prints the text inside ""
print "And finally we close it."
#Closes the file
target.close()
