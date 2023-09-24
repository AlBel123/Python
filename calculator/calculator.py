def calculator():
    import art_calculator
    print(art_calculator.calculator)
    def add(num1,num2):
        """This fucntion returns Addition result"""
        return  num1+num2
    def subtract(num1,num2):
        """This fucntion returns Substraction result"""
        return num1-num2
    def multiply(num1,num2):
        """This fucntion returns Multiplication result"""
        return num1*num2
    def divide(num1,num2):
        """This fucntion returns Division result"""
        return num1/num2
    def exponent(num1,num2):
        """This fucntion returns Exponent result"""
        return num1**num2
    operations_dict={
        "+":add,
        "-":subtract, 
        "*":multiply, 
        "/":divide, 
        "^":exponent,
        }
    num1=float(input("What is the 1st number? "))
    should_continue=True
    n=2
    while should_continue==True:
        for symbol in operations_dict:
            print(symbol)
        operation_in_dict=False
        while operation_in_dict==False:
            operation=(input("Choose the operation from the list above: "))
            if operation in operations_dict:
                operation_in_dict=True
            else:
                print("\nOperation is not valid. Please try again.")
                operation_in_dict=False
        if n==2:
            num_next=float(input("What is the 2nd number? "))
        elif n==3:
            num_next=float(input("What is the 3rd number? "))
        else:
            num_next=float(input(f"What is the {n}th number? "))
        n+=1
        answer=operations_dict[operation](num1,num_next)
        print(f"{num1}{operation}{num_next}={answer}")
        num1=answer   
        continue_choice=input(f"\nDo you want to make another calculation with {answer}? y/n ").lower()
        if continue_choice=="y":
            should_continue
        else:
            print("Thanks. Good-bye...")
            should_continue=False
            calculator()
if __name__ == '__main__':
    calculator()