# import random module
import random

# import words
from word_list import words

# setup random word
chosen_word = random.choice(words)

# setup lives start at 6
lives = 6

# setup display
display = []

# for each letter in word create "_" in display
for letter in chosen_word:
    display.append("_")

# set game condition to True
game_on = True

# begin game loop
while game_on:
    # create some spacing
    print("\n")
    # show display to user
    print(" ".join(display))

    # ask user choose a letter
    choice = input("Welke letter zit in het word? ")

    # check if user choice match word
    if choice in chosen_word:
        # # if choice match word loop over word to find letter
        for i in range(len(chosen_word)):
            # ## when found replace the  "_" in display at the correct position
            if chosen_word[i] == choice:
                display[i] = choice

    # check if "_" not in chosen word if so you win game
    if "_" not in display:
        print(f"Je hebt gewonnen! Het woord was {chosen_word}.\n")
        game_on = False

    # if choice not in chosen_word subtract 1 live
    if choice not in chosen_word:
        lives -= 1
        print(f"{lives} lives left.\n")

    # check if player have turns left if not game over
    # # stop loop
    if lives == 0:
        print(f"Game Over! Het woord was {chosen_word}.")
        # set game_on to false
        game_on = False
