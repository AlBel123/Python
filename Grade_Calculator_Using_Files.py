""" 
Grade Calculator Using Files
Author: Oleksandr Bilytskyi
Date: 17 Apr 2023

Description: This application contains data about students' names, marks and grades.
            It feeds data from the tex-file, that has a list of names, grades and marks.

            The application is manu-driven:

            1. Add new students - prompt to enter the mnumkber of students, name and mark achieved.
                It will then calculate the Grade and hold the data in 3 separate lists: names[], marks[] and Grades[].
            
            2. List the names of all students - List only the Names of students.
            
            3. Print full details - Print Names, Marks and Grades of existing and newly added students.
            
            4. Search a student by name by entering one or more letters - Entering the letter 'a' will list all the names atsrts with 'a': Andrew, Ann, Adelle etc.
                The more letters you put - the more refind is the sarch: e.i. inputting 'am' will bring Amila or Amy only.
            
            5. Add a single student - This option ads a single entry without prompting a number of students.

            6. Remove a student - Removes the Student by Name and all his data.

            7. Exit - It saves the current text file by adding the new entries and removing those removed from the list.

"""
#This is the starting point of the Application
def main():
       #Create the lists to hold names, marks, grades
    names=[]
    marks=[]
    grades=[]

    readData(names,marks,grades)
    menu(names,marks,grades)

#=====================================================================================================================

#This function is responsible for reading data from the file.
def readData(names,marks,grades):
    # Start reading data from the file line-by-line to populate the 3 lists while reading from "Grades.txt"

    with open("grades.txt", "r") as MyFile: #open the file for read-only
        for line in MyFile: # loop throgh the text file LINE-by-LINE (line in the "for line in MyFile" is just a VARIABLE - can be renamed)
            details=line.split(",") # Each time a line is read from the file, the program will split it into several parts 
                                    # separated by comas using the split() function which creates the list with the number of elements,
                                    # based on the number of comas:
                                    # e.g. 2 comas => 3 elements
            names.append(details[0].capitalize())
            marks.append(details[1])  
            grades.append(details[2].strip("\n"))
            
        print()

#=====================================================================================================================

# Displays the Menu. Prompts the user selection of the menu.
def menu(names, marks,grades):
    while True: # Loop forever untill we stop
        print("1-\t Add Students\n"
            "2-\t List all Students (by name only)\n"
            "3-\t Print full details (name, mark, grade)\n"
            "4-\t Search a Student by name (Enter one character or more characters\n"
            "5-\t Add a Student (single entry)\n"
            "6-\t Remove a Student\n"
            "7-\t Save the data and EXIT\n")

        selection=int(input("Select from the above: "))

        if (selection==1):
            print("Selection 1")
            numberOfStudents=int(input("Enter the NUMBER of Students you want to add: ")) 
        # call the Input data function passing Names, Marks, Grades and Number of Students as the Parametres
            inputData(names,marks,grades,numberOfStudents)


        elif (selection==2): # List by Names only
            print("Selection 2")
            if len(names)==0:
                input("There are NO registered students. Press ENTER to continue....")
            else:
                print(f"{names}")
                input("Press ENTER to continue....")

        elif (selection==3):
            print("Selection 3")
            if len(names)==0:
                input("There NO registered students. Pree ENTER to continue....")
            else:
                printer(names,marks,grades)
                input("Press ENTER to continue....")


        elif (selection==4):
            print("Selection 4")
            #Search student by name
            searchName(names,marks,grades)


        elif (selection==5):
            print("Selection 5")
            inputData(names,marks,grades,1)

        elif (selection==6):
            removeEntry(names,marks,grades)

        elif (selection==7):
            exportData(names, marks, grades)
            print("Thank you, Goodbye!")
            exit(0)

#=====================================================================================================================

#Propmts to enter the number of Students, then populates 3 lists (grades will be calculated)
def inputData(names,marks,grades,numberOfStudents):
    # loop as many times as the NUMBR of Students
    for i in range(numberOfStudents):
        name=input("Enter the Name of the student: ")
        names.append(name.capitalize())
        mark=int(input(f"Enter the Mark achieved by {name}: "))
        marks.append(mark)
        grade=gradeCalculator(mark)
        grades.append(grade)
        

#=====================================================================================================================

#This function establishes the grade achieved. It returns the value (grade)
#It takes a single parameter (mark), it then works out the grade:
# >=70 - A, 60-69 - B, 50-59 - C, <50 - 'Fail'

def gradeCalculator(mark):
    grade="Fail"
    if(mark>=70):
        grade="A"
    elif(mark>=60):
        grade="B"
    elif(mark>=50):
        grade="C"


    return grade


#=====================================================================================================================

# This function searches for the name in the name list.
def searchName(names,marks,grades):
    found=bool(False) # This variable will change to True if the name exists.
    letters=input(f"Enter a letter or more of the Student's name to be searched: ")
    i=0
    while i<len(names):
        if names[i].find(letters,0,len(letters))!=-1 or names[i].find(letters.capitalize(),0,len(letters))!=-1:
            print(f"{names[i]}\t {marks[i]}\t {grades[i]}\t")
            found=bool(True)
        i=i+1

    if found==bool(False):
        print("The bane natching the search is NOT found")
    input("Hit Enter to continue ...")

#=====================================================================================================================

# Removes a student by name
def removeEntry(names,marks,grades):
            if(len(names) == 0):
                input("There are no registered students! Hit enter to continue...")
            else:
                nameToBeRemoved=input(f"Enter the name of student to be removed: ").capitalize()    
                if(nameToBeRemoved in names):
                # names.remove(name)
                    index=names.index(nameToBeRemoved)
                
                    print(f"{nameToBeRemoved} sits at {index}")
                    del names[index]
                    del marks[index]
                    del grades[index]

                    input(f"{nameToBeRemoved} was removed successfully, hit Enter to continue ....")
                else:
                    print(f"{nameToBeRemoved} does not exist")
                    input("Hit Enter to continue ...")

#=====================================================================================================================

# Savesd the list to the Text File
def exportData(names,marks,grades):
    with open ("grades.txt", "w") as f:
        for i in range (len(names)):
            f.write(f"{names[i]},{marks[i]},{grades[i]}\n")

#=====================================================================================================================

# Prints the contents lists[] 

def printer(names, marks, grades):
      for i in range(len(names)):
        print(f"{i+1}. \t  Name: {names[i]}\t\t Mark achieved: {marks[i]}\t Grade achieved: \"{grades[i]}\"")
         
    
#=====================================================================================================================


if __name__=="__main__":
    main()

