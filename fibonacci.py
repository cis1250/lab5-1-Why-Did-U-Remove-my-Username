#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_positive_int():
    while True:
        user_input = input("Enter the number of Fibonacci terms to generate: ")
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print("Invalid input. Please enter a positive integer.")

def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def print_sequence(seq):
    print("Fibonacci sequence:")
    print(", ".join(str(num) for num in seq))

def main():
    n = get_positive_int()
    fib_seq = generate_fibonacci(n)
    print_sequence(fib_seq)

if __name__ == "__main__":
    main()
