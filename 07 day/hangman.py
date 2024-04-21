import random
import hangman_art
import hangman_words
import os

chosen_word = random.choice(hangman_words.word_list)

display = []
for _ in chosen_word:
    display.append("_")

i = 0
lives = 6
guessed_letters = []

print(f"{hangman_art.logo}\n")

while "_" in display:
    
    if lives > 0:
        curr_try = False
        
        guess = input("Enter letter ur guessing: ").lower()
        os.system("cls")
        
        if guess in guessed_letters:
            guess = input("U already guessed this letter. Enter some other: ").lower()
            os.system("cls")

        for char in chosen_word:
            if guess == char:
                display[i] = char
                i += 1 
                curr_try = True   
            else:
                i += 1
            
        if curr_try == True:
            print(f"{" ".join(display)}\n")            
        else:
            lives -= 1
            print(f"{guess} is a bad guess, live lost, {lives} remainig.\n{hangman_art.stages[lives]}")
            print(f"{" ".join(display)}\n")
        guessed_letters.append(guess)
        i = 0
    else:
        break

if lives > 0:
    print("WINNER")
else:
    print(f"LOOSER. Secret word was: {chosen_word}.")