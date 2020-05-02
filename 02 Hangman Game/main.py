import random
from os import system

def clear():
    system("clear")
    # system("cls") # for windows user

def randomWord():
    f = open("words.txt", 'r')
    word = random.choice(f.readlines()).lower()    
    f.close()
    return word

def playAgain():
    run = True
    while run:
        playAgain = input("Do yo want to play again (y/n) : ").lower()
        if playAgain == 'y' or playAgain == 'yes':
            play()
        elif playAgain == 'n' or playAgain == 'no':
            return True
        else:
            print("Option not found\n\n")

def play():
    attempts = 0
    max_attempts = 4
    word = list(randomWord())
    hidden = []
    for character in word:
        hidden.append("_")

    
    attempts = 0
    max_attempts = 4

    # loop until either the player has won or lost
    isGameOver = False
    while not isGameOver:
        clear()
        # display the current board, guessed letters, and attempts remaining
        print(f"You have {max_attempts - attempts} attempts remaining")

        print(f"The current word is: {' '.join(hidden)}")

        print("     ------")
        print("     |    |")
        print("     |    " + ("O" if attempts > 0 else ""))
        print("     |    " + ("/\\" if attempts > 1 else ""))
        print("     |    " + ("|" if attempts > 2 else ""))
        print("     |    " + ("/\\" if attempts > 3 else ""))
        print(" --------")

        # ask the player for a character
        letterGuessed = input("Please guess a letter: ")

        if letterGuessed in word:
            # if the player guessed correct, show all matched letters and print message
            print(f"You guessed correctly! {letterGuessed} is in the word")
            for i in range(len(word)):
                character = word[i]
                if character == letterGuessed:
                    hidden[i] = word[i]
                    word[i] = "_"
        else:
            # if player guessed wrong, print failure message and increment attempts
            print(f"You guessed wrong! {letterGuessed} is NOT in the word")
            attempts += 1

        # if the player has won print a win message and stop looping
        if all("_" == char for char in word):
            print("Congrats, you won!")
            isGameOver = playAgain()

        # if the player has lost, print failing and stop looping
        if attempts >= max_attempts:
            print("You lost, rest in peace!")
            isGameOver = playAgain()
            
def optionIntCheck(variable,minimum,maximum):
    try:
        variable = int(variable)
        if variable >= minimum and variable <= maximum:
            return variable
        else:
            print("Input number between the range!!\n> ")
    except:
        print("Input a number!!\n> ")

def addWord():
    f = open("words.txt", 'a')
    run = True
    while run:
        clear()
        print("Add new Word")
        print("="*50)
        print("1. Add")
        print("2. Exit")
        print("="*50)
        
        new = True
        while new:
            userInput = input("> ")
            userInput = optionIntCheck(userInput,1,2)

            if userInput == 1:
                newWord = input("Input new word : ")
                f.write('\n' + newWord)

                confirm = input("Add more word (y/n) : ").lower()
                if confirm == 'y' or confirm == 'yes':
                    new = False
                elif confirm == 'n' or confirm == 'no':
                    new = False
                    run = False
                else:
                    print("Option not found!! \n")
            else:
                break
    f.close()

run = True

while run:
    clear()
    print("WELCOME TO HANGMAN")
    print("="*50)
    print("1. Play")
    print("2. Add Word")
    print("3. Exit")
    print("="*50)

    userInput = input("> ")
    userInput = optionIntCheck(userInput,1,3)

    if userInput == 1:
        play()
    elif userInput == 2:
        addWord()
    else:
        run = False
