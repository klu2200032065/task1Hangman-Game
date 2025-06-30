import random

# Step 1: Predefined list of words
word_list = ['apple', 'mango', 'grape', 'peach', 'melon']
chosen_word = random.choice(word_list)  # Randomly select a word
word_length = len(chosen_word)
guessed_letters = []  # To store guessed letters
incorrect_guesses = 0
max_incorrect = 6

# Step 2: Create a display with underscores
display = ['_'] * word_length

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Step 3: Main game loop
while incorrect_guesses < max_incorrect and '_' in display:
    print("\nCurrent word:", ' '.join(display))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Good guess!")
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! You have {max_incorrect - incorrect_guesses} tries left.")

# Step 4: Game result
if '_' not in display:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game over! The word was:", chosen_word)
