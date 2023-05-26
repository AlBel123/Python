
""" 
    File: Maths OPs
    Author: Mahmood
    Date: 13 March 2023
    Description: Timestable program
"""
def main():
    print("The program starts here......")
    number1=int(input("Enter a number: "))
    number2=int(input("Enter another number: "))
    
    #Prompt the user to enter a sign
    
    sign= (input("Select a number from the following\nA- Addition\nB- Subtraction \nC- Multiplcation \nD- Division\nE- Exit the program\n"))
    if(sign=="A"):
      add(number1,number2)
    
    elif(sign=="B"):
       subtract(number1,number2)
       
    elif(sign=="C"):
      multiply(number1,number2)
    
    elif(sign=="D"):
       divide(number1,number2) 
    
    else:
        print("Please enter a valid selection")
        
    
def add(number1,number2):
    print()
    print(f"{number1} + {number2} = {number1 + number2}")
    
def subtract(number1,number2):
    print()
    print(f"{number1} - {number2} = {number1 - number2}")
def multiply(number1,number2):
    print()
    print(f"{number1} x {number2} = {number1 * number2}")
def divide(number1,number2):
    print()
    print(f"{number1} / {number2} = {number1 / number2}")
#Everytime your python program runs it creates a variable called __name__
#If thigs run correctly, then the value of __name__ is equal to the string 
"__main__"
#We'll use this condition to call the main() function as the starting point of our program
if __name__=="__main__":
    main()
