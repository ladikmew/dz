a = 'apple'

def game():
    print('Hi, you have 5 tries to guess the world')
    part1 = ""

    tries = 5
    while tries>0:
        sorried = 0
        for l in a:
            if l in part1:
                print(l, end=" ")
            else:
                print("*", end=" ")
                sorried += 1

        if sorried == 0:
            print("\nYou win!")
            break

        player = input("\nLetter:")
        part1 += player

        if player not in a:
            tries -= 1
            print("\nYou missed :(", end=' ')
            print("\nYou have", tries, "tries")
        if player in a:
            print('Keep up the good work!')
    # нет сообщения о проигрыше.


if __name__  =="__main__":
    b = "yes"
    while b == "yes":
        game()
        print('Do you like to play again?')
        b = input()

