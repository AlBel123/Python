#================ Hangman ==================================================================


import words_hangman
import art_hangman
import random
import os

print(f"\n{art_hangman.logo}")
word=random.choice(words_hangman.word_list)
# print(word)


encrypted_word=[]
for letter in range(0,len(word)):
    # print(word[i])
    symbol="_"
    encrypted_word.append(symbol)
print(f"\n{encrypted_word}")


attempt=6
number_of_guessed=0

guesses=[]
while attempt>0 and number_of_guessed<len(word):
    guess=input("\nInput Letter: ").lower()
    os.system('cls')
    if guess in guesses:
        print(f"You have tried the letter '{guess}' already! try another one")
        print(f"{art_hangman.stages[attempt]}\n")
        print(f"The letters already tried: {guesses}")
        attempt=attempt
        
    else:
        guesses.append(guess)
        if guess=="":
            print("This filed cannot be Void!. Please start again")
            exit(0)
        nmbr_char=word.count(guess)
        if nmbr_char>=1:
            attempt=attempt
            number_of_guessed+=nmbr_char
            print(f"You guessed {number_of_guessed} letters out of {len(word)}!")
            print(f"{art_hangman.stages[attempt]}\n")
            if number_of_guessed>=len(word):
                print(f"Congratulations!  You Won!\n The word was '{word.upper()}'.")
                exit(0)
            else:
                pass
        else:
            attempt-=1
            print (f"There is no letter '{guess}' in the word!")
            print(f"{art_hangman.stages[attempt]}\n")

            if attempt==0 and number_of_guessed<len(word):
                print(f"You lost the game! the word was '{word.upper()}'.\n GAME OVER!")  
                exit(0)
            else:
                pass   
        print(f"The letters already tried: {guesses}")

    for letter in range(0,len(word)):
        
        if guess==word[letter]:
            # print (f"You guessed '{word[i]}' in the position {[i]}")
            encrypted_word.pop(letter)
            encrypted_word.insert(letter,guess) 
        else:
            pass
  
    print(encrypted_word) 
    print (f"you have {attempt} wrong attempts yet")   

