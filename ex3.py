n=18
no_of_guess=1
while(no_of_guess<=9):
    inp = int(input("Please guss the number\n"))
    if inp<18:
        print("You num is smaller")

    elif inp>18:
        print("your number is grater")
    else :
        print("You are correct")
        print(no_of_guess,"no.of guesses he took to finish.")
        break
    print(9-no_of_guess,"no of guess left")
    no_of_guess = no_of_guess+1

if(no_of_guess>9):
    print("game over")
