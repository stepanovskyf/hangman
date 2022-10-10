import requests
import random
from new_words import stages
from new_words import word_list

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
used = []

display = []
lives = 6
end_point = ""
word = random.choice(word_list)
word = word.lower()
word_length = len(word)
for _ in range(word_length):
    if _ == " ":
        display += " "
    else:
        display += "_"
while "_" in display:
    if lives > 0:
        guess = input("Guess a letter: ").lower()
        if guess in word:
            if guess in display:
                print("You are correct... But you already guessed this letter")
            print("Yes! That is correct!")
            for position in range(word_length):
                letter = word[position]
            #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
                if letter == guess:
                    display[position] = letter
                elif letter == " ":
                    display[position] = " "
            print(display)
            used.append(guess)
            print(f"Letters you used are {used}")
        else:
            lives -= 1
            print("I am sorry, that is incorrect")
            print(stages[lives])
            used.append(guess)
            print(f"Letters you used are {used}")
    else:
        end_point = "N"
        break
if end_point == "N":
    print("You lose!")
else:
    print("You won!")