print('''
                                                   _____
                                                ,-'_____`-.
                                              ,',-'     `-.`.
                                             /,' _       _ `.\
                                            // ,' `.   ,' `. \\
                                           j l//"| |   | |"\\j l
                                           |  /  | |   | |  \  |
         A      A      A      A      A     | `---' `---' `---' |     A      A      A      A      A
        j l    j l    j l    j l    j l    | ,---. ,---. ,---. |    j l    j l    j l  ,-=+=-.  j l
        | |    | |    | |    | |    | |    | |   | |   | |   | |    | |    | |    | | j <> <> L | |
        | |    | |    | |    | |    | |    | |   | |   | |   | |    | |    | |    | | J   o   F | |
        |_|    |_|    |_|    |_|    |_|   _|_|   | |   | |   | |    |_|    |_|    |_|  `.MWM,'  |_|
       (___)==(___)==(___)==(___)==(___)==[__|   | |   | |   | []==(___)==(___)==(___)==(___)==(___)
        | |    | |    | |    | |    | |   "| |   | |   | |   | ||   | |    | |    | |    | |    | |
        | |    | |    | |    | |    | |    | `---' `---' `---'[_|   | |    | |    | |    | |    | |
        |_|    |_|    |_|    |_|    |_|   _|_,---. ,---. ,---. ||   |_|    |_|    |_|    |_|    |_|
       (___)==(___)==(___)==(___)==(___)==[__|   | |   | |   | []==(___)==(___)==(___)==(___)==(___)
        | |    | |    | |    | |    | |   "| |   | |   | |   | |    | |    | |    | |    | |    | |
        | |    | |    | |    | |    | |    | |   | |   | |   | |    | |    | |    | |    | |    | |
        |_|____|_|____|_|____|_|____|_|____|_|___|_|___|_|___|_|____|_|____|_|____|_|____|_|____|_|AZR''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

move = input("What's your next move? ")
if move == "Right":
    print("Fell into a hole. Game over.")
elif move == "Left":
    move = input("Swim or wait? ")
    if move == "Swim":
        print("Attacked by trout. Game over.")
    elif move == "Wait":
        move = input("Which door? ")
        if move == "Red":
            print("Burned by fire. Game over.")
        elif move == "Blue":
            print("Eaten by beasts. Game over.")
        elif move == "Yellow":
            print("You win!")
        else:
            print("Game Over.")
