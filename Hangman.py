import random
from hangman_words import word_list
from hangman_arts import logo
from hangman_arts import stages

key_word = random.choice(word_list)
print(f"Psst..Your key_word is {key_word}")
blank = []
print(logo)
word_length = len(key_word)
for cnt in range(word_length):
    blank.append("_")
print(blank)
print(stages[6])
end_of_game = False
life = 6
control = []
while not end_of_game and life >= 0:
    guess = input("Guess a letter: ").lower()
    if guess not in control:
        control.append(guess)
    else:
        print(f"You've already guessed {guess}")
        life += 1
    for counter in range(word_length):
        if guess in key_word[counter]:
            blank[counter] = guess
    if guess not in key_word:
        life -= 1
        print(stages[life])
        if life <= 0:
            end_of_game = True
            print("You Lose...")
    print(blank)
    if not '_' in blank:
        end_of_game = True
