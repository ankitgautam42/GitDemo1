file = open("test.txt")   # we need the paas the location of the file.
#print(file.read())  # read all the contents of file

#print(file.read(2))  # print n number of character from file by passing parameter

#print(file.readline()) # read one single line at a time using readline method.
#print(file.readline())

#line = file.readline()
#while line != "":
#    print(line)
#   line = file.readline()

#print(file.readlines())
for line in file.readlines():
    print(line)

file.close()