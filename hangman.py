import random
Game = True                             #the game starts
charnum = 0                             #the number of characters in the searched word
gcharnum = 0                            #the number of characters in the guessed word 
while Game == True:                     #While Game is true, the program gets executed
    Word = ["world","universe","ball"] #those are the words which are able to be searched
    activeWord = (random.choice(Word))  #a random word gets picked 

    for char in activeWord:             #for every char of the searched word...
       print ("/")                      #... gets a character printed out as an slash
       charnum = charnum + 1            #... a 1 gets added to the 'charnum'

    guess = input()                     #the guess of the player 
    for char in guess:                  #for every char in the guess...
        gcharnum = gcharnum + 1         #... a 1 gets added

    if gcharnum == 1:                   #if just one character got guessed
        if guess.lower() in activeWord: #right guess
            print ("Right letter")
            quit()
        else:                           #wrong guess
            print ("That letter isn't in the Word")
            quit()
    elif gcharnum >= 1:                 #if the word got guessed 
        if guess.lower() == activeWord: #if the word was guessed right
            print("That's the word!")
            quit() 
        elif guess.lower() != activeWord: #if the word was guessed wrong 
            print("That's the wrong word.")
            quit()