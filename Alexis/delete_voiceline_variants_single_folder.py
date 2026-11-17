import os
import os.path

mypath = input("Path: ")
contents = [f for f in os.listdir(path=mypath) if os.path.isfile(os.path.join(mypath, f))]
#folders = os.listdir(path=mypath)
#folder_counter = 0
#new_path = os.path.join(mypath, folders[folder_counter])

#print(folders)
#print(folders[folder_counter])
#print(new_path)
#contents = [f for f in os.listdir(path=new_path) if os.path.isfile(os.path.join(new_path, f))]
print(contents)

option = input("Continue? ")

separator = input("Separator to look for: ")
while option != 'n':
    mypath = input("Path: ")

    #folders = os.listdir(path=mypath)
    
    #new_path = os.path.join(mypath, folders[folder_counter])

    contents = [f for f in os.listdir(path=mypath) if os.path.isfile(os.path.join(mypath, f))]
    #contents = [f for f in os.listdir(path=new_path) if os.path.isfile(os.path.join(new_path, f))]

    print(contents)

    #option = input("Continue? ")
    if option != 'n':

        #separator = input("Separator to look for: ")
        #change = input("Value to replace it for: ")

        #original = None
        for file in contents:
            if ".1.ogg" in file:
                original = file.split(separator)
                print(original)
                os.rename(os.path.join(mypath, file), os.path.join(mypath, original[0] + original[1]))

        print("\n\n", contents)


        contents = [f for f in os.listdir(path=mypath) if os.path.isfile(os.path.join(mypath, f))]
        for file in contents:
            if ".2.ogg" in file or ".3.ogg" in file or ".4.ogg" in file or ".5.ogg" in file:
                os.remove(os.path.join(mypath, file))

    #folder_counter += 1
    #print(folder_counter)