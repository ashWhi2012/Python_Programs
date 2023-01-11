#Ashton Whitt, CSC 220, 4/22/2022, Use dictionaries to reformat old labs

#Reworking track coach lab:

def create_file(file):
    '''
    This function is only used in the case that the file has nothing stored on
    it, or if the user would like to recreate the file. File parameter should
    be a string.

    It has one parameter, the file name. The file will be cleared of all data,
    and will allow the user to enter new data for the students.

    The function does not return anything.
    '''
    fo = open(file, 'w')
    fo.close()
    
    dic = {}       
    print("Name and personal records will be stored in the following way: \
Name of student, Personal record")
    s_name = input("What is the name of the first student you would to enter \
data for? Repeat names are not accepted. (Enter to stop) ")
    while s_name:
        s_record = input("What is the students record? ")
        while True:
            try:
                f_record = float(s_record)
                break
            except:
                s_record = input("Not a valid time input, try again: ")
                
        dic[s_name] = s_record
        s_name = input("Enter the student's name: (Enter to stop) ")
        while s_name in dic:
            s_name = input("That name is currently in use, input a new name: ")

    s_write_to_file = ""
    for key in dic:
        s_write_to_file += key + "," + dic[key] + "\n"

    fw = open(file, "w")
    fw.write(s_write_to_file)
    fw.close()
        

def make_dict(file):
    '''
    This function has one input paramater, the name of a file.

    This function takes a comma separated variable file and returns a dictionary
    based on the information in the file. The file being used also has each
    data point separated by an end line.
    '''
    fo = open(file, 'r')
    s_line = fo.readline()
    s_name = ""
    s_time = ""
    d = {}
    while s_line:
        b_comma = True
        i = 0
        while i < len(s_line):
            if s_line[i] == ",":
                b_comma = False
                
            if s_line[i] != "," and b_comma == True:
                s_name += s_line[i]

            elif s_line[i] != "," and b_comma == False:
                s_time += s_line[i]

            i += 1

        d[s_name] = s_time
        s_line = fo.readline()
        s_name = ""
        s_time = ""

    fo.close()

    return d

def edit_file(dic, file):
    '''
    This function has two parameters. The first is a dictionary and the second
    is the name of a file.

    The function updates the dictionary based on user input and then updates the
    file correspondingly. The function is able to edit the records of students
    in the file.

    No value is returned.
    '''
    s_name = input("What is the name of the student whose data you would like \
to edit? ")
    while True:
        try:
            s_old_time = dic[s_name]
            break
        
        except:
            s_name = input("That name is not valid, try again: ")
            
    f_old_time = float(s_old_time)
    print(f"{s_name}'s old time was: {dic[s_name]}")
    s_new_time = input("What is the new time of the student? ")
    while True:
        try:
            f_new_time = float(s_new_time)
            break

        except:
            s_new_time = input("That was not a valid time, try again: ")
    
    if f_new_time < f_old_time:
        dic[s_name] = s_new_time + "\n"

    else:
        print("That time was not better than their previous.")

    s_write_file = ""
    for key in dic:
        s_value = dic[key]
        s_write_file = s_write_file + key + "," + s_value

    fo = open(file, 'w')
    fo.write(s_write_file)
    fo.close()


def remove_student(dic, file):
    '''
    This function has two parameters. The first is a dictionary and the second
    is the name of a file.

    The function updates the dictionary based on user input and then updates the
    file correspondingly. The function is used for removing students from the
    file.

    No value is returned.
    '''
    s_name = input("What is the name of the student whose data you would like \
to edit? ")
    while True:
        try:
            s_old_time = dic[s_name]
            break
        
        except:
            s_name = input("That name is not valid, try again: ")
            
    del dic[s_name]

    s_write_file = ""
    for key in dic:
        s_value = dic[key]
        s_write_file = s_write_file + key + "," + s_value

    fo = open(file, 'w')
    fo.write(s_write_file)
    fo.close()


def look_time(dic):
    '''
    This function has one parameter, a dictionary.

    The function outputs the record of a student contained in a file based on
    the user input.

    No value is returned.
    '''
    s_name = input("What is the name of the student whose data you would like \
to look at? ")
    while True:
        try:
            s_old_time = dic[s_name]
            break
        
        except:
            s_name = input("That name is not valid, try again: ")
            
    print(f"{s_name}'s current record is {dic[s_name]}")


def add_student(dic, file):
    '''
    This function requires two parameters. The first parameter is the
    dictionary that will be referenced. The second parameter is the string
    value that is the name of a file being written to.

    This function adds a student to the end of the file by gathering user
    input.

    Nothing is returned from the function.
    '''
    s_name = input("What is the name of the student who you would like to add? ")
    while s_name in dic:
        s_name = input("That name is currently in use, input a new name: ")

    s_time = input("What is their record in seconds? ")
    #using try and except:
    while True:
        try:
            f_time = float(s_time)
            break

        except:
            s_time = input("That was not a valid time, try again: ")
    
    dic[s_name] = s_time + "\n"
    s_write_to_file = ""
    for key in dic:
        s_write_to_file += key + "," + dic[key]

    fo = open(file, 'w')
    fo.write(s_write_to_file)
    fo.close()


def get_input():
    '''
    Function has no parameters.

    Function is called whenever an input is needed for what type of action the
    user wants to perform.

    Function returns the users input as a string.
    '''
    s_input = input("Would you like to add, edit, remove, or look at \
student data? Type 'add' 'edit' 'remove' or 'look' (Enter to stop) ")
    s_input.lower()
    while (s_input != "add" and s_input != "edit" and s_input != "remove" and
           s_input != 'look' and s_input != ""):
        s_input = input("You did not enter 'add', 'edit', 'remove', or 'look' \
please try again. (Enter to stop) ")
        s_input = s_input.lower()

    return s_input
    

def main():
    file_name = "students_pr.txt"
    while True: #If the program has not been used before, allows the user to
#write a starting file and formats it correctly.
        try:
            fo_b = open(file_name, 'r')
            break
        except:
            print("This file has not been used before, the file will now be \
created and you will be able to enter names and their times until you want to \
stop.")
            create_file(file_name)

    s_input = get_input()
    while s_input:
        names_dict = make_dict(file_name) #updates dictionary during each loop
            #iteration
        if s_input == 'add':
            add_student(names_dict, file_name)

        elif s_input == 'remove':
            remove_student(names_dict, file_name)

        elif s_input == 'look':
            look_time(names_dict)

        elif s_input == 'edit':
            edit_file(names_dict, file_name)

        s_input = get_input()
        
main()         
