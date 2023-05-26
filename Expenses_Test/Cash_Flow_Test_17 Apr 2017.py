"""
File Name: Cash_Flow_Test
Author: Oleksandr Bilytskyi
Description: App is meant to read data from the file and calculate the cash-flow 
Operations Menu: 1. Add data
                2. Show the months
                3. Show the full list
                4. Add One entry
                5. Delete Entry
                6. Search for the Entry
                7. Exit
"""


def main():
    
    months=[]
    incomes=[]
    expenses=[]
    balances=[]

    read(months,incomes,expenses,balances)
    menu(months,incomes,expenses,balances)
#==============================================================================
def read(months,incomes,expenses,balances):
    print("The Data from file was read and uploaded...")

    with open("Cash_Flow.txt","r") as MyFile:
        for line in MyFile:
            details=line.split(",")

            months.append(details[0])
            incomes.append(details[1])
            expenses.append(details[2])
            balances.append(details[3].strip("\n"))
        

        
#==============================================================================

def menu(months,incomes,expenses,balances):
    while True:
        print("Main menu:\n1. Add data \n2. Show the months \n3. Show the full list\n4. Add One entry\n5. Delete Entry\n6. Search for the Entry\n7. Exit")
        selection=int(input("Please enter your choice from the list above: "))

        if selection==1:
            print("Selection = 1")
            numberOfMonths=int(input("Enter Number of Months to be added: "))
            inputData(months,incomes,expenses,balances,numberOfMonths)
        
        elif selection==2:
            if len(months)==0:
                input("There is NO registered data. Press ENTER to continue....")
            else:
                print(f"{months}")
                input("Press ENTER to continue....")


        elif selection==3:
            print("Selection = 3")
            if len(months)==0:
                input("There is NO registered data. Press ENTER to continue....")
            else:
                printer(months,incomes,expenses,balances)

        elif selection==4:
            print("Selection = 4")

        elif selection==5:
            print("Selection = 5")

        elif selection==6:
            print("Selection = 6")

        elif selection==7:
            print("Selection = 7")
            exit(0)

    

#==============================================================================

def inputData(months,incomes,expenses,balances,numberOfMonths):

    for i in range (numberOfMonths):
        month=input(f"Enter the name of the month: ")
        months.append(month)
        income=int(input(f"Enter the Income in {month}: "))
        incomes.append(income)
        expense=int(input(f"Enter the Expenses in {month}: "))
        expenses.append(expense)
        balance=balanceCalculator(month,income,expense)
        balances.append(balances)


# def inputData(names,marks,grades,numberOfStudents):
#     # loop as many times as the NUMBR of Students
#     for i in range(numberOfStudents):
#         name=input("Enter the Name of the student: ")
#         names.append(name.capitalize())
#         mark=int(input(f"Enter the Mark achieved by {name}: "))
#         marks.append(mark)
#         grade=gradeCalculator(mark)
#         grades.append(grade)
#==============================================================================

def balanceCalculator(month,income,expense):
    print("I am balanceCalculator")
    balance=income-expense
    print(f"Balance in {month} is {balance}")

#==============================================================================
def printer(months,incomes,expenses,balances):
        
        for i in range(len(months)):
            print(f"{i+1}. \t  {months[i]}\t\t Income: {incomes[i]}\t Expenses: {expenses[i]}\t Balance:{balances[i]}")

        input("Press ENTER to continue....")


#==============================================================================    
def deleteEntry():
    print("I am deleteEntry")
#==============================================================================

def export():
    print("I am Export")

#==============================================================================

def searchItem():
    print("I am Search")

#==============================================================================

if __name__=="__main__":
    main()
