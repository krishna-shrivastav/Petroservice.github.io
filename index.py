import random

def number_guessing_game():

    print(" Welcome to the Number Guessing Game!")
    print("Maine 1 se 100 ke bich ek number socha hai ab aapko wo number chunna hai.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_input = input(" Enter your guess: ")

        if not user_input.isdigit():
            print(" Invalid input. Please enter a number between 1 and 100.")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < 1 or guess > 100:
            print(" 1 se 100 tak koi number chune")
        elif guess < secret_number:
            print("Abhi kam hai. Dobara kosis kare")
        elif guess > secret_number:
            print("Abhi jyada hai.Dobara kosis kare")
        else:
            print(f" Badhai ho! AAPNE SAHI NUMBER CHOONA HAI {attempts} attempts me .")
            break

if __name__ == "__main__":
    number_guessing_game()
