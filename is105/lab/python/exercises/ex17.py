#Gets the sys package and imports the argv feature from this package.
from sys import argv
#Gets the os.path package and imports the exists feature from this package. This feature returns 'True' if the file exists and 'False' if not.
from os.path import exists

#Defines the argument variables as script, from_file and to_file.
script, from_file, to_file = argv

#Prints the text inside "" and adds the two definitions we just wrote.
print "Copying from %s to %s" % (from_file, to_file)

#Creates a variable called "in_file". This variable opens the file we defined in from_file. In this case it's out test file "ex17-test.txt"
in_file = open(from_file)
#Creates a variable called "indata". This variable reads the file we just opened.
indata = in_file.read()

#Prints the text inside "" and adds %d, which gets a decimal number variable, and puts in len(indata). THis is a function to display file size of the chosen file (indata).
print "The input file is %d bytes long" % len(indata)

#Prints the text inside the "". Asks if the "to_file" exists. It doesn't, so it returns 'False'. This is due to the exist feature we imported from os.path.
print "Does the output file exist? %r" % exists(to_file)
#Prints the text inside the ""
print "Ready, hit RETURN to continue, CTRL-C to abort."
#Pauses the script until we either press RETURN or CTRL-C.
raw_input()

#Creates a variable called out_file which opens the to_file in write mode. This makes it possible to copy what is written in out file to the new file.
out_file = open(to_file, 'w')
#Copies the file to the new file by writing what is being read() (indata) to the new file.
out_file.write(indata)

#Prints the text inside the ""
print "Alright, all done."

#Closes the out_file
out_file.close()
#Closes the in_file
in_file.close()
