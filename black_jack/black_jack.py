def black_jack():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    cards_player=[]
    cards_comp=[]
    import random
    import art_black_jack
    import os

    print(art_black_jack.title)

    def ace_check(layout):
        position_ace=layout.index(11)
        layout.pop(position_ace)
        layout.insert(position_ace,1)
        return layout
    

    i=0
    while i < 2:
        cards_player.append(random.choice(cards))
        i+=1
    j=0
    while j<2:
        cards_comp.append(random.choice(cards))
        j+=1
    print(f"\nYour cards are {cards_player} and your Score is {sum(cards_player)}")
    print(f"1st Dealer's card is [{cards_comp[0]}]. He keeps {j} cards.")

    while sum(cards_comp)<17:
        j+=1
        cards_comp.append(random.choice(cards))
        y=cards_comp.count(11)
        if sum(cards_comp)>21 and y>0:
            print(ace_check(cards_comp))
        print(f"\nDealer takes 1 more card...Apperently, he had less than 17 points before that... Now he keeps {j} cards.")

    should_continue=True
    while should_continue:
        x=cards_player.count(11)
        if sum(cards_player)<=21:
            take_card=input("\nType 'y' to get another card or 'n' to pass: ")
            if take_card=="n":
                print(f"\nYour Final Hand is {cards_player} with the Score {sum(cards_player)}\nDealer's Final Hand is {cards_comp} with the Score {sum(cards_comp)}")
                should_continue=False
                if sum(cards_player)>sum(cards_comp) or (sum(cards_player)<=sum(cards_comp) and sum(cards_comp)>21):
                    print("You Win!")
                elif sum(cards_player)<sum(cards_comp) and sum(cards_comp)<=21:
                    print("Dealer Wins!")
                elif sum(cards_player)==sum(cards_comp) and sum(cards_comp)<=21:
                    print("Draw!")
                else:
                    print("some other option... check the software")
            else:
                cards_player.append(random.choice(cards))
                if x>0:
                    print(f"Ace is counted as '1' point now! Your cards are {ace_check(cards_player)} and your Score is {sum(cards_player)}")
                else:
                    print(f"\nYour cards are {cards_player} and your Score is {sum(cards_player)}")
                    print(f"1st Dealer's card is still [{cards_comp[0]}]. He keeps {j} cards.")
                should_continue
        elif sum(cards_player)>21:
                
                if x>0:
                    print(f"Ace is counted as '1' point now! Your cards are {ace_check(cards_player)} and your Score is {sum(cards_player)}")

                    
                else:
                    print(f"\nYour Final Hand is {cards_player} with the Score {sum(cards_player)}\nDealers's Final Hand is {cards_comp} with the Score {sum(cards_comp)}")
                    print("\nDealer Wins!")
                    should_continue=False
    new_game_choice=input("\n\nPlay again? y/n: ").lower()
    if new_game_choice=="y":
        os.system("cls")
        black_jack()
    else:
        print("Good-bye...")
        exit(0)

black_jack()


