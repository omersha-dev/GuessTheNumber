# This project was built by Omer Sha'ashua in order to practice python and coding.
# This is a game in which the computer chooses a number and the user needs to guess it.
# The user is first promoted to choose the difficulty level which in accordance the range
# of the numbers the computer is allowed to choose from and the amount of attempts the user
# has to guess the right number is decided.
#
# In order to make the game as flawless as possible, there are input validation methods
# to ensure the player will not be able to make the game crash.
#
# If you found anything problematic, have an idea on how to improve the game either by code
# or by adding some functionality, please let me know.
# You can view this project on GitHub: https://github.com/omersha-dev/GuessTheNumber

import random

class Game:

    def __init__(self):
        self.attemptsTried = 0
        self.startGame()
        self.difficulty = self.setDifficulty()
        self.attemptsAmount = self.setAttemptsAmount()
        self.maxRange = self.setMaxRange()
        self.chosenNumber = self.generateRandomNumber()
        self.gameCourse()

    def setMaxRange(self):
        tempMaxRange = 1
        for i in range(0, self.difficulty):
            tempMaxRange *= 10
        print("The number the computer has chose is between 0 and %d" % tempMaxRange)
        return tempMaxRange

    def generateRandomNumber(self):
        return random.randrange(0, self.maxRange)

    def startGame(self):
        print("""Hello!
Welcome to this awesome game in which the computer chooses a number
and you have to guess it (otherwise you DIE MUHAHAHA)\n""")

    def setDifficulty(self):
        difficulty = input("""Please choose the difficulty:
    1. Easy
    2. Normal
    3. Hard\n""")
        difficulty = self.allowOnlyInt(difficulty)
        while(difficulty < 1 or difficulty > 3):
            difficulty = self.allowOnlyInt(input("Please choose one of the difficulties mentioned above\n"))
        return difficulty

    def setAttemptsAmount(self):
        if(self.difficulty == 1):
            return 3
        elif(self.difficulty == 2):
            return 10
        elif(self.difficulty == 3):
            return 15

    def allowOnlyInt(self, input):
        try:
            temp = int(input)
            return temp
        except:
            return -1

    def validateInputNumber(self, input):
        input = int(input)
        if(input >= 0 and input <= self.maxRange):
            return self.checkInput(input)
        else:
            print("Please enter a number between 0 and %d" % self.maxRange)
            return False

    def checkInput(self, input):
        self.attemptsTried += 1
        if(input == self.chosenNumber):
            print("That is current! You win!")
            return True
        elif(input > self.chosenNumber):
            print("The number is smaller then %d" % input)
            return False
        else:
            print("The number is bigger then %d" % input)
            return False

    def gameCourse(self):
        guessedNumber = self.validateInputNumber(self.allowOnlyInt(input("You have %d attempts. Try and guess the computer's number!\n" % self.attemptsAmount)))
        while(guessedNumber == False or guessedNumber == -1):
            print("You have %d attempts remaining\n" % (self.attemptsAmount - self.attemptsTried))
            if(self.attemptsTried >= self.attemptsAmount):
                print("You had too many attempts and you have failed, the computer wins! (and you must die now...)")
                break
            guessedNumber = self.validateInputNumber(self.allowOnlyInt(input()))

def main():
    game = Game()

if __name__ == "__main__":
    main()