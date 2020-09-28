import random

#variables
randomWord = ""
outputWord = ""
mistakesLeft = 0
index = 0
inputChar = ''
categoryNum = 0
categoryName = ""
difficultyNum = 0
difficultyName = ""
listToString = ' '
wrongLetters = " "

#Welcomes user and prompts for category choice
print("Hello, welcome to hangman!")
categoryNum = int(input("Choose your category - Enter 1 for Animals, 2 for Colors, 3 for Country Names: "))
#Processes user input for category choice and chooses random word from file
if(categoryNum < 1 or categoryNum > 3):
    print("Sorry, that is not a valid category choice. Please re-run the program and try again!")
    exit()
if(categoryNum == 1):
    categoryName = "Animals"
    randomWord = random.choice(open("animals.txt").read().split("\n"))
elif(categoryNum == 2):
    categoryName = "Colors"
    randomWord = random.choice(open("colors.txt").read().split("\n"))
elif(categoryNum == 3):
    categoryName = "Country Names"
    randomWord = random.choice(open("countries.txt").read().split("\n"))

#Prompts user to choose difficulty
difficultyNum = int(input("Choose your difficulty - Enter 1 for easy (7 strikes), 2 for medium (5 strikes), 3 for hard (3 strikes): "))
#Sets category name to the user input
if(difficultyNum < 1 or difficultyNum > 3):
    print("Sorry, that is not a valid difficulty choice. Please re-run the program and try again!")
    exit()
if(difficultyNum == 1):
    difficultyName = "Easy"
    mistakesLeft = 7
elif(difficultyNum == 2):
    difficultyName = "Medium"
    mistakesLeft = 5
elif(difficultyNum == 3):
    difficultyName = "Hard"
    mistakesLeft = 3

#Prints category and difficulty to user
print("You chose to play " + categoryName + " on " + difficultyName + '.')

#processes chosen word into a list
randomWord = randomWord.lower()
outputWord = list(randomWord)
while(index < len(outputWord)):
    if(outputWord[index] != ' '):
        outputWord[index] = "_"
    index = index + 1
listToString = ' '.join([str(elem) for elem in outputWord])

#processes user input until word is correct or lives run out
wrongLetters = list(wrongLetters)
print(listToString)
while mistakesLeft > 0 and "_" in outputWord:
    inputChar = input("Please enter a letter (" + str(mistakesLeft) + " mistakes left): ")
    if(inputChar in outputWord):
        print("The letter " + inputChar + " has already been guessed correctly.")
        continue
    elif (inputChar in wrongLetters):
        print("The letter " + inputChar + " has already been guessed incorrectly.")
        continue
    if(inputChar in randomWord):
        for index in range(0, len(randomWord)):
            if(randomWord[index] == inputChar):
                outputWord[index] = inputChar
        listToString = ' '.join([str(elem) for elem in outputWord])
        print(listToString)
    else:
        print("Sorry, " + inputChar + " was not in the word.")
        print(listToString)
        wrongLetters.append(inputChar)
        mistakesLeft = mistakesLeft -1


if(mistakesLeft == 0):
    print("Sorry! The word was \"" + randomWord + "\". Better luck next time!")
    exit()
elif("_" not in outputWord):
    print("Congrats! The word was \"" + randomWord + "\". Great job!")
    exit()    
