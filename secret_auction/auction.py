import art_auction
import os
print(art_auction.gavel)

print("Welcome to SECRET AUCTION!")

auction_dict={}
should_continue=True
while should_continue==True:
    name=input("Please indicate your name: ").capitalize()
    bid=int(input("Please give your Bid: $"))
    auction_dict[name]=bid
    print(auction_dict)

    choice_continue=input("Are there any other participants? (y/n): ").lower()
    os.system('cls')
    if choice_continue=="n":
        should_continue=False

    max=0
    for name in auction_dict:
        if auction_dict[name]>max:
            max=auction_dict[name]
            winner=name

print(f"Max Bid is {max} made by {winner}")