# Simple Letter Guessing Game (Hangman-like)

word = "python"  # The word to guess
guessed_letters = []
attempts = 6  # Number of wrong guesses allowed

print("Welcome to the Letter Guessing Game!")
print("Guess the word by suggesting letters.")
print(f"The word has {len(word)} letters.")

while attempts > 0:
    # Display the current state
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print(display.strip())

    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! {attempts} attempts left.")

if attempts == 0:
    print("Sorry, you ran out of attempts. The word was:", word)
