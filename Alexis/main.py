import os
import os.path

mypath = input("Path: ")
contents = [f for f in os.listdir(path=mypath) if os.path.isfile(os.path.join(mypath, f))]

print(contents)

option = input("Continue? ")


while option != 'n':
    mypath = input("Path: ")
    contents = [f for f in os.listdir(path=mypath) if os.path.isfile(os.path.join(mypath, f))]

    print(contents)

    option = input("Continue? ")
    if option != 'n':

        separator = input("Separator to look for: ")
        change = input("Value to replace it for: ")

        for file in contents:
            original = file.split(separator)
            print(original)
            os.rename(os.path.join(mypath, file), os.path.join(mypath, original[0] + change + original[1]))

        print("\n\n", contents)