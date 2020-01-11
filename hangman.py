import random
from time import sleep

Game = True                             #the game starts

goodpoint = 0                           #the points you need to win get defined
badpoint = 0                            #the points you need to loose get defined

Word = ["world","universe","ball"]      #those are the words which are able to be searched
activeWord = (random.choice(Word))      #a random word gets picked 
for char in activeWord:
    pointsneeded = pointsneeded + 1     #how many points you need to win/lose

while Game == True:                     #While Game is true, the program gets executed
    gcharnum = 0                        #'gcharnum' gets reset/set to 0
    charnum = 0                         #'charnum' gets reset/set to 0

    for char in activeWord :            #for every character of the searched word...
       print ("/")                      #... gets a character printed out as an slash
       charnum = charnum + 1            #... a 1 gets added to the 'charnum'

    guess = input()                     #the guess of the player 
    for char in guess:                  #for every character in the guess...
        gcharnum = gcharnum + 1         #... a 1 gets added

    if gcharnum == 1:                   #if just one character got guessed
        if guess.lower() in activeWord: #right guess
            print ("Right letter")
            goodpoint = goodpoint + 1
        elif guess.lower() not in activeWord: #wrong guess
            print ("That letter isn't in the Word")
            badpoint = badpoint + 1     #1 badpoint is getting added
    elif gcharnum >= 1:                 #if the word got guessed 
        if guess.lower() == activeWord: #if the word was guessed right
            print("That's the word!")
            quit() 
        elif guess.lower() != activeWord: #if the word was guessed wrong 
            print("That's the wrong word.")
            quit()             
    
    if badpoint == (pointsneeded):
        print("You lost.")
        sleep (0.5)
        print ("The word was "+ str(activeWord))
        quit()
    if goodpoint == (pointsneeded):
        print ("You Won!")
        sleep (0.5)
        print ("the word was "+ str(activeWord))