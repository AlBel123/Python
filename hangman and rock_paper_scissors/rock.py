#========= Rock, Paper, Scissors ============================================================

import os 

def print_rock():
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

def print_paper():
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

def print_scissors():
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

def gameMenu():
    
    x=0
    y=0
    while x<3 and y<3:
        customerChoice=input("Please make your choice:\n1.Rock\n2.Paper\n3.Scissors\n")
        customerChoice=customerChoice.lower()
        if customerChoice=="1" or customerChoice=="rock":
            print("Player's Choice: Rock")
            print_rock()
        elif customerChoice=="2" or customerChoice=="paper":
            print("\nPlayer's Choice: Paper")
            print_paper()
        elif customerChoice=="3" or customerChoice=="scissors":
            print("\nPlayer's choice: Scissors")
            print_scissors()
        else:
            print("\nChoice is not valid!\n")
            gameMenu()
         
        import random
        computerChoice=random.randint(1, 3)
       
        if computerChoice==1:
            print("Computer's choice: Rock")
            print_rock()
        elif computerChoice==2:
            print("Computer's choice: Paper")
            print_paper()
        elif computerChoice==3:
            print("Computer's choice: Scissors")
            print_scissors()
    
        if customerChoice=="1" or customerChoice=="rock": 
            if computerChoice==1:
                print("Draw!")
            elif computerChoice==2:
                print("Computer wins the round!")
                x=x+1
            elif computerChoice==3:
                print("Player wins the round!")
                y=y+1
                
        elif customerChoice=="2" or customerChoice=="paper": 
            if computerChoice==1:
                print("Player Wins the round!")
                y=y+1
            elif computerChoice==2:
                print("Draw!")   
            elif computerChoice==3:
                print("Computer wins the round!")
                x=x+1
                
        elif customerChoice=="3" or customerChoice=="scissors":
            if computerChoice==1:
                print("Computer Wins the round!")
                x=x+1
            elif computerChoice==2:
                print("Player Wins the round!") 
                y=y+1
            elif computerChoice==3:
                print("Draw!")

        print(f"\nThe score is {y}:{x}\n ")
        input("\nPress ENTER key to continue\n")
        os.system('cls')
        print(f"\nThe score is {y}:{x}\n ")
        if x==3:
            print("Computer wins the Game!\nGame over")
            exit(0)
        elif y==3:
            print("Player wins the Game!\nGame over")
            exit(0)
        
if __name__ == '__main__':
    gameMenu()