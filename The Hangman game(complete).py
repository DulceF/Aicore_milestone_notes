#M2 T1 Define the list of possible words

word_list = ["banana", "kiwi", "avocado", "apple", "pear"]
print(*word_list)

#M2 T2 Choose a random word from the list
import random 
print(random.choice(word_list))

#M2 T3 Ask the user for input
guess = input("Guess a letter")

#M2 T4 Check that the input is a single character

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("That is not a valid input")
#M3 T1 Iteratively check if the input is a valid guess 

guess = input("Guess a letter")
while True:
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical charachter")

#M3 T2 Check whether the guess is in the word
if guess in word_list:
    print("Goode guess! {guess} is in the word.")
else:
    print("Sorry, {guess} is not in the word. Try again.")

#M3 T3 Create functions to run the checks
def check_guess(guess):
    lowercase = guess.lower()    
   
def ask_for_input():
   guess = input("Guess a letter")
while True:
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical charachter")
ask_for_input() 


#M4 Create the game class
#M4 T1 Create the class
class Hangman:
    def __init__(self, word, word_list, num_lives, word_guessed, num_letters, list_of_guesses):
        import random
        self.word = word
        self.word_list = word_list
        self.num_lives = 5
        self.word_guessed = ["_","_","_","_","_"]
        self.num_letters = num_letters
        self.list_of_guesses = []

#M4 T2 Create methods for running the checks
word_list = ["banana", "kiwi", "avocado", "apple", "pear"]
import random 
print(random.choice(word_list))

def check_guess(guess):                            
    guess = input("Guess a letter")
    guess = guess.lower()  
                            
secretword = (random.choice(word_list))
if guess in secretword:                         
    print("Good guess! {guess} is in the word") 

check_guess(guess) 

def ask_for_input(guess):
    list_of_guessess = [] 
    from typing import List
        
    while True:                                     
        guess = input("Guess a letter")                
        if len(guess) != 1 and guess != guess.isalpha:  
            print("Invalid letter. Please enter a single alphabetical character")

        elif guess in list_of_guessess(guess):                 
            print("You already tried that letter")      
        else:
            check_guess(guess)
        
ask_for_input(guess)  #When calling this it shows up as error : NameError: name 'list_of_guesses' is not defined????

#M4 T3 Define what happens if the letter is in the word
                           
def check_guess(guess):                                  
    guess = input("Guess a letter")
    guess = guess.lower()                           
    secretword = (random.choice(word_list))
         
    for word_guessed in word_list:                    #M4 T4 Define what happens if the letter is NOT in the word
        if word_guessed == guess:                            
                index = word_guessed.index(guess)
                print("Good guess! {guess} is in the word") 
                break
        else: num_lives -= 1
        print("Sorry, {letter} is not in the word. You have {num_lives} left.")
list_of_guesses.append(guess)   
num_letters -= 1

# M5 T1 Code the logic of the game

def play_game(word_list):
        Hangman()
Hangman = game(word_list, num_lives)

#Pass word_list and num_lives as arguments to the game object ?????????
while True:
        if num_lives == 0:
            print("You lost!")
        elif num_letters >0:
            ask_for_input()
        else: 
            num_lives != 0
            print("Congratulations. You won the game!")
            
play_game(word_list)
