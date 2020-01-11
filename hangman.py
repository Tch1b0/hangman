import random
from time import sleep

Game = True                             #the game starts

pointsneeded = 0                        #the amount of points you need to win/lose
goodpoint = 0                           #the points you need to win get defined
badpoint = 0                            #the points you need to loose get defined
repeated_chars = []                     #the characters that shouldn't get repeated are getting added right here
right_chars = []                        #the right characters are getting saved in this list
wrong_chars = []                        #the wrong characters are getting saved in this list
space = ("*****")                       #this is the definition for the space between some text

Word = [                                #those are the words which are able to be searched (You shouldn't use words which contain the same character more than one time)
"world","bike","cloud","orange","car",
"house","garden","space","duck","goose",
"smartphone","smart","mouse","airplane"
]                                      
activeWord = (random.choice(Word))      #a random word gets picked 
for char in activeWord:                 #for every character existing in the word you 
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
    print (space)                       #a space between 
    sleep(0.5)                          
    print ("right characters",str(right_chars)) #the right guessed characters get here displayed
    sleep(0.25)                                 #a short delay in order to look more smooth
    print("_____")                              #this is suposed to look like a brake between those displayed informations
    sleep(0.25)                                 #a short delay in order to look more smooth
    print("wrong characters",str(wrong_chars))  #the wrong guessed characters get here displayed
    print (space+"\n")

    guess = input()                     #the guess of the player 
    sleep (0.75)
    for char in guess:                  #for every character in the guess...
        gcharnum = gcharnum + 1         #... a 1 gets added

    if gcharnum == 1:                   #if just one character got guessed

        if guess in repeated_chars: #if the character was already guessed
            print ("You already had this one\n")
            print (space)
            sleep (1)
            badpoint = badpoint + 1     #1 'badpoint' is getting added
            repeated = True             #the other cases below get deactivated for the round

        if guess.lower() in activeWord and repeated == False:      #right guess
            print ("Right character\n")
            print (space)
            sleep (1)
            goodpoint = goodpoint + 1   #1 'goodpoint' is getting added
            repeated_chars += [guess]   #the guess gets added to the 'repeated_chars' list and can't get guessed again
            right_chars += [guess]      #the character is getting added to the right character list
            

        elif guess.lower() not in activeWord and repeated == False: #wrong guess
            print ("That character isn't in the Word\n")
            print (space)
            sleep (1)
            badpoint = badpoint + 1     #1 'badpoint' is getting added
            repeated_chars += [guess]   #the guess gets added to the 'repeated_chars' list and can't get guessed again
            wrong_chars += [guess]      #the wrong character is getting added to the 'wrong_chars' list 



    elif gcharnum >= 1:                 #if the word got guessed 
        if guess.lower() == activeWord: #if the word was guessed right
            print("That's the word!")
            goodpoint = pointsneeded    #the needed amount of points you need to win is getting filled up, so you win instantly

        elif guess.lower() != activeWord: #if the word was guessed wrong 
            print("That's the wrong word.")
            badpoint = pointsneeded     #the needed amount of points you need to lose is getting filled up, so you lose instantly 

    
    if goodpoint == (pointsneeded):     #if you get every character of the word you win
        endscreen("won",0.5)            #winning endscreen gets activated 

    if badpoint == (pointsneeded):      #if you got as much mistakes like the word has characters, you lose
        endscreen("lost",0.5)           #lose screen gets activated