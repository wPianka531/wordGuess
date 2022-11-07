#word guess game based one 30 random words
#walter pianka
#11/3/2022
import random
with open('words.txt') as f:
    #variable start
    character1 = False
    character2 = False
    character3 = False
    character4 = False
    character5 = False
    guess = []
    x = 0
    #selects a random word from the list and turns it into a list
    filelist = list(f.readlines())
    randomWord = random.choice(filelist).strip()
    wordCharacters = list(randomWord.strip())
    #variable end
    #instructions
    print("""this is a word guessing game. 
    the word has five letters and you have ten guesses to find each letter.
    There can be duplicate letters.
    Once you know the letters you have to find the word.
    Good luck and have fun!""")
    for i in range(11):
        #ends loop if the answer is correct
        if character1 and character2 and character3 and character4 and character5:
            print ("you have guessed all the letters!")
            break
        x+=1
        #ends loop if you don't guess all of the correct letters
        if x == 11:
            print ("you have lost the game :(")
            print ("please try again")
            break
        print ("guess a letter")
        letter = input()
        #checks for letters in a way that will notify you that you have 2+ of the same letter
        if letter == wordCharacters[0]:
            character1 = True
            print ("you have guessed a character")
            guess.append(letter)
        if letter == wordCharacters[1]:
            character2 = True
            print ("you have guessed a character")
            guess.append(letter)
        if letter == wordCharacters[2]:
            character3 = True
            print ("you have guessed a character")
            guess.append(letter)
        if letter == wordCharacters[3]:
            character4 = True
            print ("you have guessed a character")
            guess.append(letter)
        if letter == wordCharacters[4]:
            character5 = True
            print ("you have guessed a character")
            guess.append(letter)
        if letter != wordCharacters[0] and letter != wordCharacters[1] and letter != wordCharacters[2] and letter != wordCharacters[3] and letter != wordCharacters[4]:
            print(letter, "is not one of the letters") 
        print ("you have guessed the following letters correctly")
        print (guess)
    if x<11:
        x=0
        #instructions for part 2
        print("""Congrats! you have guessed all the correct letters.
        Please organize these letters into the correct word.
        You have three guesses.
        Here are your letters""")
        print(guess)
        #finds out if you guessed the right word in three tries
        for i in range(4):
            x+=1
            if x == 4:
                print ("you have lost. try again")
                break
            print("what is your", x , "guess?")
            wordGuess = input()           
            if wordGuess.lower().strip() == randomWord:
                print("Congratulations! You Win!")
                break
            else:
                print("wrong answer")