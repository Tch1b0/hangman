import random
from time import sleep

Game = True                             #the game starts

pointsneeded = 0                        #the amount of points you need to win/lose
goodpoint = 0                           #the points you need to win get defined
badpoint = 0                            #the points you need to loose get defined
repeated_chars = []

Word = ["world","universe","ball"]      #those are the words which are able to be searched
activeWord = (random.choice(Word))      #a random word gets picked 
for char in activeWord:
    pointsneeded = pointsneeded + 1     #the amount of points to win/lose gets defined

def endscreen(text,delay):              #the screen you see when you finish the game gets defined
    print ("You "+(text)+"!")
    sleep (delay)
    print ("the word was "+ str(activeWord)) #you can see what word you had to guess 
    quit()


while Game == True:                     #While Game is true, the program gets executed
    gcharnum = 0                        #'gcharnum' gets reset/set to 0
    charnum = 0                         #'charnum' gets reset/set to 0
    repeated = False                    #resetting repeated

    for char in activeWord :            #for every character of the searched word...
       print ("/")                      #... gets a character printed out as an slash
       charnum = charnum + 1            #... a 1 gets added to the 'charnum'

    guess = input()                     #the guess of the player 
    for char in guess:                  #for every character in the guess...
        gcharnum = gcharnum + 1         #... a 1 gets added

    if gcharnum == 1:                   #if just one character got guessed

        if guess in repeated_chars:     #if the character was already guessed
            print ("You already had this one")
            badpoint = badpoint + 1     #1 'badpoint' is getting added
            repeated = True             #the other cases below get deactivated for the round

        if guess.lower() in activeWord and repeated == False:      #right guess
            print ("Right letter")
            goodpoint = goodpoint + 1   #1 'goodpoint' is getting added
            repeated_chars += [guess]   #the guess gets added to the 'repeated_chars' list and can't get guessed again

        elif guess.lower() not in activeWord and repeated == False: #wrong guess
            print ("That letter isn't in the Word")
            badpoint = badpoint + 1     #1 'badpoint' is getting added
            repeated_chars += [guess]   #the guess gets added to the 'repeated_chars' list and can't get guessed again



    elif gcharnum >= 1:                 #if the word got guessed 
        if guess.lower() == activeWord: #if the word was guessed right
            print("That's the word!")
            goodpoint = pointsneeded
        elif guess.lower() != activeWord: #if the word was guessed wrong 
            print("That's the wrong word.")
            badpoint = pointsneeded      

    
    if goodpoint == (pointsneeded):     #if you get every character of the word you win
        endscreen("won",0.5)            #winning endscreen gets activated 

    if badpoint == (pointsneeded):      #if you got as much mistakes like the word has characters, you lose
        endscreen("lost",0.5)           #lose screen gets activated