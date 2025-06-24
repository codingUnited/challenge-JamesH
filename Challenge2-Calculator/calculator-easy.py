class OperationError(Exception):
    def __init__(self, message="Please select a valid operation (+, -, *, /): "):
        super().__init__(message)

def validate_input(value):
    if value not in {'+','-','*','/'}:
        raise OperationError()

class DivideByZero(Exception): 
    def __init__(self, message="Please don't try to divide by zero. "):
        super().__init__(message)

def divisionLogicCheck(value, operator):
    if operator == '/' and value == 0:
        raise DivideByZero()

def main():
    print("Welcome to your calculator!")

    while True:
        num1 = input("Enter the first number: ")
        try: 
            num1 = float(num1)
            break
        except ValueError:
            print("Invalid entry. Please enter a number.")

    while True:
        operator = input("Enter an operation (+, -, *, /): ")
        try: 
            validate_input(operator)
            break
        except OperationError as e:
            print(e)

    while True: 
        num2 = input("Enter the second number: ")
        try: 
            num2 = float(num2)
            divisionLogicCheck(num2, operator)
            break
        except ValueError:
            print("Invalid entry. Please enter a number.")
        except DivideByZero as e:
            print(e)

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2

    print(f"Result: {result}")

if __name__ == "__main__":
    main()