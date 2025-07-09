
def add_name():

    file = open('names.txt', 'a')
    for _ in range(1, 3 + 1):
        names = input("Enter the name to add: ").strip().title()
        file.write(names + '\n')
    file.close()

def read_names():
    file = open("names.txt", "r")
    names = file.readlines()
    for _ in names:
        print(_.rstrip())
    file.close()


   
add_name()
read_names()
# This code adds names to a file and reads them back.
# It uses a simple text file to store names, allowing for easy addition and retrieval.
# The add_name function appends names to 'names.txt', while read_names reads and prints them.
# The code is straightforward and serves as a basic example of file handling in Python.