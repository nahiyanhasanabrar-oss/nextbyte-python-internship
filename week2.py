# Week 2: Loops, Functions & Problem Solving


def get_valid_int(prompt, min_val=None, max_val=None):
    """Validate integer input with optional min/max range."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Please enter a number >= {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Please enter a number <= {max_val}.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


# 1. Multiplication Table Generator (Loop + Function)
def generate_multiplication_table(number, limit=10):
    print(f"\n--- Multiplication Table for {number} ---")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")


# 2. Sum of Even Numbers up to N (Loop + Function)
def sum_even_numbers(n):
    total = 0
    for num in range(2, n + 1, 2):
        total += num
    return total


# 3. Factorial Calculator (Loop + Function)
def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 4. Vowel Counter in a String (Loop + Function)
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


# 5. Number Guessing Game with Limited Attempts (While Loop + Function)
def number_guessing_game(secret_number=7, max_attempts=3):
    print(f"\n--- Guess the Number (1 to 10) | Attempts: {max_attempts} ---")
    attempts = 0
    while attempts < max_attempts:
        guess = get_valid_int(f"Attempt {attempts + 1} - Enter your guess: ", 1, 10)
        attempts += 1
        if guess == secret_number:
            print(f"Correct! You guessed it in {attempts} attempt(s).")
            return
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
    print(f"Out of attempts! The number was {secret_number}.")


def main():
    print("=== NextByte Studio - Week 2 Problem Solving ===")

    # Problem 1
    table_num = get_valid_int("\n[1] Enter a number for multiplication table: ", 1, 100)
    generate_multiplication_table(table_num)

    # Problem 2
    even_limit = get_valid_int("\n[2] Enter a positive number for even sum (up to N): ", 1, 10000)
    print(f"Sum of even numbers from 1 to {even_limit}: {sum_even_numbers(even_limit)}")

    # Problem 3
    fact_num = get_valid_int("\n[3] Enter a non-negative number for factorial: ", 0, 20)
    print(f"Factorial of {fact_num}: {calculate_factorial(fact_num)}")

    # Problem 4
    sentence = input("\n[4] Enter a text to count vowels: ").strip()
    while not sentence:
        print("Text cannot be empty!")
        sentence = input("[4] Enter a text to count vowels: ").strip()
    print(f"Total vowels: {count_vowels(sentence)}")

    # Problem 5
    number_guessing_game(secret_number=7, max_attempts=3)


if __name__ == "__main__":
    main()