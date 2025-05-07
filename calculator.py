#!/usr/bin/env python3
"""
Simple calculator module that adds two numbers.
"""

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def main():
    """Main function to run the calculator interactively."""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        result = add_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Please enter valid numbers.")
    except KeyboardInterrupt:
        print("\nCalculator exiting.")

if __name__ == "__main__":
    main() 