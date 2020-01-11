import random
Game = True

if Game == True:
    Word = ["World","Universe"]
    activeWord = (random.choice(Word))

    #for char in activeWord:
    #    print(char, char.isalpha())

    for char in activeWord:
        print ("/")

    guess = input()
    for cahr in activeWord:
        print(char, char.isalpha)
