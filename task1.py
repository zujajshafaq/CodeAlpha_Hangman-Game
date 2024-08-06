import random

def hangman():
    # List of words to choose from
    wordschoice = ["artificial", "intelligence", "machine", "learning", "beauty", "code", "algorithm", "data", "science"]
    word = random.choice(wordschoice)
    guessed_word = ["_"] * len(word)
    guessed_letters = []
    attempts = 6

    print("WELCOME TO HANGMANn!")
    print(" ".join(guessed_word))
    print(f"You have {attempts} incorrect guesses allowed.")

    while attempts > 0 and "_" in guessed_word:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("Already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print("Incorrect guess.")
        
        print(" ".join(guessed_word))
        print(f"Guess letters: {', '.join(guessed_letters)}")
        print(f"Incorrect guess left: {attempts}")

    if "_" not in guessed_word:
        print("Congratulations! You've guessed the word:", word)
    else:
        print("Attempts Finished. The word was:", word)

if __name__ == "__main__":
    hangman()
