"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
print('\n')
f = open('src/foo.txt', 'r')
print(f.read())
f.close()
print('\n')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

file = open('bar.txt', 'w')

file.write('Once upon a time Billy went to college, got a degree he no longer uses and got on millon dollars in debt. Now he eats rice cakes to survive and has to recycle his own urine to drink')

file.close()

file = open('bar.txt', 'r')
print(file.read())
print('\n')

# YOUR CODE HERE
