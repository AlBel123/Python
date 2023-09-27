import random
import art_guess
import os


print("\nWelcome to my Guess Number Game!\U0001F617\n\nI am thinking about the digit between 1 and 100.")

def game():
    print(art_guess.title)
    NUMBER=random.randint(1,100)
    # print(NUMBER)

    difficulty=input("\nChoose the difficulty level: type 'Hard' or 'Easy' ").lower()
    if difficulty=="easy":
        attempts=10
        
    elif difficulty=="hard": 
        attempts=5
    else:
        os.system("cls")
        print("Please make your choice...")
        game()
    print(f"You have {attempts} attempts to guess the number!")

    should_continue=True
    while should_continue==True:
        guess=int(input("\nEnter your guess: "))
        attempts-=1
        if attempts==0:
            print(f"Game over! You have no attempts! \U0001f62d\n {art_guess.game_over}")
            should_continue=False
        elif guess==NUMBER:
            print(f"Well done! \U0001f600   You guessed the number! I thought of {NUMBER}")
            should_continue=False
        elif guess<NUMBER:
            print(f"Too small! \U0001FAF3   You have {attempts} attempts")
            should_continue
        elif guess>NUMBER:
            print(f"Too big! \U0001faf4   You have {attempts} attempts")
            should_continue

    continue_choice=input("\n\ndo you want to play again? y/n: ").lower()
    if continue_choice=="y":
        os.system("cls")
        game()
        
    else:
        print(f"Thanks! good-bye...\n {art_guess.game_over}")
        exit(0)

if __name__ == '__main__':
    game()

