import random

# Basic arithmetic functions are defined here - add, divide, subtract and multiply. 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Fun facts - just to add a unique-ish element in this
fun_facts = [
    "Did you know? The first mechanical calculator was invented in 1642 by Blaise Pascal.",
    "Did you know? Python was named after the television show Monty Python's Flying Circus.",
    "Did you know? The first computer virus was created in 1983 and was called 'Elk Cloner'.",
    "Did you know? The number 0 was independently invented by the Mayans and Indians.",
    "Did you know? Ada Lovelace is considered the first computer programmer.",
    "Did you know? Python is an interpreted language, which means it is executed line by line.",
    "Did you know? Calculators today are millions of times more powerful than the Apollo 11 guidance computers.",
    "Did you know? The equals sign '=' was invented in 1557 by Robert Recorde.",
    "Did you know? The Fibonacci sequence is found in many aspects of art, nature, and architecture.",
    "Did you know? The first electronic computer, ENIAC, weighed more than 27 tons and took up 1800 square feet."
]

#so that the fun facts can actaully be displayed:
def get_fun_fact():
    return random.choice(fun_facts)

# Main program loop - introduction
def main():
    print("Welcome to the Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
  
#take inputs
    while True:
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")

        if choice == 'q':
            print("Goodbye! Have a nice day!")
            break
#enter values for calculator
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue
#perform the required operation, eg. add, subtract, etc.
            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")

            print(get_fun_fact())
        else:
            print("Invalid Input")

#in order to repeat the program again 
if __name__ == "__main__":
    main()

#and thats all! my first time writing a longer program, and using the 'import' function <3
