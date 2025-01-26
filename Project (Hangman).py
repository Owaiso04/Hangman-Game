import random

logo = """
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"                               
"""

stages = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]

stages.reverse()
words_list = (
    "ant baboon badger bat bear beaver camel cat clam cobra cougar "
    "coyote crow deer dog donkey duck eagle ferret fox frog goat "
    "goose hawk lion lizard llama mole monkey moose mouse mule newt "
    "otter owl panda parrot pigeon python rabbit ram rat raven "
    "rhino salmon seal shark sheep skunk sloth snake spider "
    "stork swan tiger toad trout turkey turtle weasel whale wolf "
    "wombat zebra "
).split()

print(logo)

chosen_word = random.choice(words_list)
chosen_word_list = ["_" for _ in chosen_word]

lives = 6
guess_list = []

while "_" in chosen_word_list and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess not in guess_list:
        guess_list.append(guess)
        correct_guess = False

        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                chosen_word_list[i] = guess
                correct_guess = True

        if not correct_guess:
            print(f"You guessed {guess}, that's not in the word, you lose a life.")
            lives -= 1
    else:
        print(f"You've already guessed {guess}")

    print(stages[lives])
    print(" ".join(chosen_word_list))

if "_" not in chosen_word_list:
    print("You win!")
else:
    print("You lose! The word was:", chosen_word)
