
import random
import game_data
import art
import os

# random choice for Hero1


def choose_hero():
    heroes=game_data.data
    hero=heroes[random.randint(0,len(heroes)-1)]
    
    return(hero)

hero1=choose_hero()


#compare
def game():
    should_continue=True
    score=0
    while should_continue:
        print(art.logo)
        if score>0:
            print((f"\nYou are right! Current score: {score}"))
        global hero1
        print(f"\n\nCompare A: {hero1['name']}, {hero1['description']}, from {hero1['country']}.")
        print(art.vs)
        hero2=choose_hero()
        print(f"\nAgainst B: {hero2['name']}, {hero2['description']}, from {hero2['country']}.")
        # print(hero1['follower_count'])
        # print(hero2['follower_count'])
    
        wrong_choice=True
        while wrong_choice==True:
            choice=input("Who has more followers? Type A or B: ").lower()
            if choice=="a":
                chosen_hero=hero1
                other_hero=hero2
                wrong_choice=False
            elif choice=="b":
                chosen_hero=hero2
                other_hero=hero1
                wrong_choice=False
            else:
                print("Make your choice! Enter A or B.")
                wrong_choice

        if (chosen_hero['follower_count'])>=(other_hero['follower_count']):
            score+=1
            hero1=chosen_hero
            should_continue
            os.system('cls')
            

          
        else:
            os.system('cls')
            print(art.logo)
            print(f"\nSorry, that's wrong! Your final score is {score}.")
            should_continue=False
            play_again=input("\n\nDo you want to play once more? y/n: ").lower()
            if play_again=="y":
                os.system('cls')
                game()
            else:
                print("Good-bye...")
                exit()



if __name__=='__main__':
    game()
