import random

def draw_step1():
    print("_______")
    print("|/     ")
    print("|      ")
    print("|      ")
    print("|      ")
    print("|      ")
    print("|")
    print("|___")

def draw_step2():
    print("_______")
    print("|/      |")
    print("|        ")
    print("|        ")
    print("|        ")
    print("|        ")
    print("|")
    print("|___")

def draw_step3():
    print("_______")
    print("|/      |")
    print("|      (_)")
    print("|         ")
    print("|         ")
    print("|         ")
    print("|")
    print("|___")

def draw_step4():
    print("_______")
    print("|/      |")
    print("|      (_)")
    print("|       | ")
    print("|       ")
    print("|       ")
    print("|")
    print("|___")

def draw_step5():
    print("_______")
    print("|/      |")
    print("|      (_)")
    print("|      \| ")
    print("|       ")
    print("|       ")
    print("|")
    print("|___")

def draw_step6():
    print("_______")
    print("|/      |")
    print("|      (_)")
    print("|      \|/")
    print("|       ")
    print("|       ")
    print("|")
    print("|___")

def draw_step7():
    print("_______")
    print("|/      |")
    print("|      (_)")
    print("|      \|/")
    print("|       |")
    print("|        ")
    print("|")
    print("|___")

def draw_step8():
    print("_______")
    print("|/      |")
    print("|      (_)")
    print("|      \|/")
    print("|       |")
    print("|      / ")
    print("|")
    print("|___")

def draw_step9():
    print("_______")
    print("|/      |")
    print("|      (_)")
    print("|      \|/")
    print("|       |")
    print("|      / \\")
    print("|")
    print("|___")

def draw_hangman(step):

    if (step == 1):
        draw_step1()
    elif (step == 2):
        draw_step2()
    elif (step == 3):
        draw_step3()
    elif (step == 4):
        draw_step4()
    elif (step == 5):
        draw_step5()
    elif (step == 6):
        draw_step6()
    elif (step == 7):
        draw_step7()
    elif (step == 8):
        draw_step8()
    elif (step == 9):
        draw_step9()

def create_partial_word(word, letters):

    partial_word = ""

    # copy hidden word into partial word but replace all letters that aren't found yet with dashes.
    for i in range(0, len(word)):
        if word[i] in letters:
            partial_word += word[i]
        else:
            partial_word += '-'

    return partial_word


# Create a list of words.  The computer will hide one of these, randomly.
#words = ['banana', 'chair', 'cloud', 'television', 'book', 'table', 'building', 'laptop', 'computer', 'python']
infile = open("wordlist.txt", 'r')
words = infile.readlines()

# pick a random word from the words list.  Given that the words come from a file, remove any newline characters from
# the end.
wordCount = len(words)
randomWordIndex = random.randrange(0, wordCount)
word = words[randomWordIndex]
word = word.replace('\n', '')

guessedLetters = []

# Uncomment if you want to see what word the computer chose.
#print(word)

MAX_ALLOWED_MISSES = 9 # how many times can you guess incorrectly.

misses = 0
tries = 0

while True:

    # add one to the number of times we have tried.
    tries += 1

    # ask player to guess a letter.
    letter = input("Try " + str(tries) + ": Guess a letter (" + "".join(guessedLetters) + "):")

    # add the letter to the list of letters that have been guessed so far.
    if (letter not in guessedLetters):
        guessedLetters.append(letter)

    # create a partial word from the list of guessed letters.
    partialWord = create_partial_word(word, guessedLetters)

    if (letter not in word):

        misses = misses + 1
        draw_hangman(step = misses)

    # show the partial word to the player.
    print(partialWord)

    # if the player got all the letters, then the partial word will not be partial anymore.
    # In that case, tell the player that they won.  We're done.
    # Otherwise, if the player has tried the maximum number of attempts, then tell them that
    # they lost the game.
    # If the player has not guessed all the letters and has not exceeded the maximum number of
    # attempts, then let them try again.
    if partialWord == word:
        print("You win!")
        break
    elif MAX_ALLOWED_MISSES == misses:
        print("You lose! Is it that hard to guess '" + word + "'?")
        break



