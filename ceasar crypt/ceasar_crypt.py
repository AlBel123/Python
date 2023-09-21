#============= Caesar Crypt ==================================================================

def ceasar(text, shift,direction, should_continue):
    answer=""
    if direction=="decode":
        shift *=-1
    for char in text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position+shift
            answer+=alphabet[new_position]
        else:
            answer+=char
    print(f"The {direction}d text is '{answer}'")
    restart=input("Do you want to run the Cripto again? y/n ")
    restart=restart.lower()
    if restart=="y":
        os.system('cls')
    else:
        print("Good-bye...")
        should_continue=False

    

import os
alphabet=["a", "b", "c", "d","e","f", "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a", "b", "c", "d","e","f", "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def cypher():
    should_continue=True
    while should_continue==True:
        import ceasar_art
        print(f"\n\n{ceasar_art.logo}")
        direction=input("\n\nType 'encode' to encrypt or 'decode' to decrypt:\n")
        if direction!="encode" and direction!="decode":
            print(f"Combination '{direction}' is not known command for the system. Please try again and make the correct choice. ")
            
        else:
            text=input("Input your message: ").lower()
            shift=int(input("Input the Shift number:\n"))
            shift=shift%26
            print(f"The Shift you entered is too big. CRIPTO reassigned automatically Shift to {shift}")
            ceasar(text, shift, direction, should_continue)


if __name__=="__main__":
    cypher()
