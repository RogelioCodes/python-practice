def take_input():
    while True:
        choice1 = input("Player 1 choose rock, paper, or scissors: ").lower()
        if choice1 != 'rock' and choice1 != 'paper' and choice1 != 'scissors':
            print("Invalid input")
            continue
        else:
            while(True):
                choice2 = input("Player 2 choose rock, paper, or scissors: ").lower()
                if choice2 != 'paper' and choice2 != 'rock' and choice2 != 'scissors':
                    print("Invalid input")
                    continue
                elif choice1 == choice2:
                    print("Draw, Try again")
                    continue
                else:
                    a = [choice1, choice2]
                    return a
a = take_input()
choice1 = a[0]
choice2 = a[1]


if choice1 == 'rock' and choice2 == 'scissors' or choice1 == 'scissors' and choice2 == 'paper' or choice1 == 'paper' and choice2 =='rock':
    print("Player 1 wins: ", choice1, "beats", choice2)
else:
    print("Player 2 wins",choice2, "beats", choice1)
