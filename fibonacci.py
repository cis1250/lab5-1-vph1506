#!/usr/bin/env python3
def is_positive_integer(value):
  try:
    number = int(value)
    return number > 0
  except ValueError:
    return False

def get_positive_integer():
    for _ in range(5): 
        user_input = input("Please enter a positive number: ")
        if is_positive_integer(user_input):
          return int(user_input)
        else:
          print("Please enter a positive whole integer.")
    print("Too many invalid attempts.")
    return None

def fibonacci_sequence(n):
    first = 0
    second = 1
    for _ in range(n):
        print(first, end="")
        next_number = first + second
        first = second
        second = next_number
    print()
    
def main():
    for _ in range(5): 
        n = get_positive_integer()
    if n is not None:
        fibonacci_sequence(n)
    else:
      print("Skipping Fibonacci sequence due to invalid input.")

if __name__ == "__main__":
    main()

# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
