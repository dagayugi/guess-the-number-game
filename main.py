""" Subject from "Recursion": "Guess the number game". 
"""

import random

def guess_the_number_game():
    """ Guess the number game programe """

    min, max = _request_input()

    while min > max:
        print("The minimum value must be less than or equal to the maximum value. Please enter again.")
        min, max = _request_input()

    answer = random.randint(min, max)
    print(f"Random numbers were generated in the range {min} to {max}. Let's guess.")
    
    max_num_attempts = (max - min) // 2

    for num in range(max_num_attempts):
        guess_num = int(input(
            f"Please enter a number to guess. (Number of attempts remaining {max_num_attempts - num}: "
        ))
        if guess_num == answer:
            print("Correct answer.")
            return
        elif guess_num < answer:
            print(f"Bigger than {guess_num}.")
        else:
            print(f"Smaller than {guess_num}")
    
    print(f"Too bad the correct answer is {answer}.")

def _request_input():
    """ Requests minimum and maximum value input """

    min = int(input("Please enter the minimum value: "))
    max = int(input("Please enter the maximum value: "))

    return min, max

if __name__ == "__main__":
    guess_the_number_game()
