import random


def random_number_game():
    print("Welcome to the Random Number Guessing Game!")

    # Set the range for the random number (adjust as needed)
    min_number = 1
    max_number = 100
    secret_number = random.randint(min_number, max_number)

    attempts = 0

    while True:
        user_guess = input(f"Guess a number between {min_number} and {max_number}: ")

        # Validate that the user input is a valid integer
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break


if __name__ == "__main__":
    random_number_game()
