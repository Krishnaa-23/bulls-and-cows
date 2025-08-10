import random

def generate_number():
    """Generates a random 4-digit number from 1-9 with no repeats."""
    digits = random.sample(range(1, 10), 4)
    return ''.join(map(str, digits))

def is_valid_guess(guess):
    """Checks if guess is a valid 4-digit number from 1-9 with no repeats."""
    return (
        guess.isdigit() and
        len(guess) == 4 and
        all(ch != '0' for ch in guess) and
        len(set(guess)) == 4
    )

def bulls_and_cows(secret, guess):
    """Calculates bulls and cows."""
    bulls = sum(secret[i] == guess[i] for i in range(4))
    cows = sum((ch in secret) and (secret[i] != guess[i]) for i, ch in enumerate(guess))
    return bulls, cows

def main():
    secret_number = generate_number()
    # Uncomment this for testing:
    # print(f"Secret: {secret_number}")

    print("Welcome to Bulls and Cows!")
    print("Guess the 4-digit number (digits 1-9, no repeats).")

    while True:
        guess = input("Enter your guess: ").strip()
        if not is_valid_guess(guess):
            print("Invalid guess! Make sure it's 4 unique digits (1-9).")
            continue

        if guess == secret_number:
            print("🎉 Congratulations! You guessed the number!")
            break

        bulls, cows = bulls_and_cows(secret_number, guess)
        print(f"{bulls} Bulls, {cows} Cows")

if __name__ == "__main__":
    main()
