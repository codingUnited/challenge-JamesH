class OperationError(Exception):
    def __init__(self, message="Please select a valid operation (+, -, *, /): "):
        super().__init__(message)

def validate_input(value):
    if value not in {'+','-','*','/'}:
        raise OperationError()

class Clear(Exception):
    def __init__(self, message="Memory Cleared"):
        super().__init__(message)

def clear_input(value):
    if value == "clear":
        raise Clear()

class Exit(Exception):
    def __init__(self, message="Exiting Calculator"):
        super().__init__(message)

def exit_input(value):
    if value == "exit":
        raise Exit()

class DivideByZero(Exception): 
    def __init__(self, message="Please don't try to divide by zero. \n Result unchanged."):
        super().__init__(message)

def divisionLogicCheck(value, operator):
    if operator == '/' and value == 0:
        raise DivideByZero()

def getNum(context='default'):
    while True:
        num = input("Enter a number: ").strip().lower()
        try: 
            clear_input(num)
            exit_input(num)
            num = float(num)
            break
        except ValueError:
            print("Invalid entry. Please enter a number.")
        except Clear as e:
            if context == 'num1':
                print(e)
                continue
            elif context == 'num2':
                print(e)
                return "clear"
    return num

def main():
    print("Welcome to your calculator!")
    num1 = getNum("num1")
    while True: 
        while True:
            operator = input("Enter an operation (+, -, *, /, clear, exit): ").strip().lower()
            try: 
                clear_input(operator)
                exit_input(operator)
                validate_input(operator)
                num2 = getNum("num2")
                if num2 == "clear":
                    num2 = 0
                    operator = '+'
                    num1 = getNum("num1")
                break
            except OperationError as e:
                print(e)
            except Clear as e:
                num1 = 0
                operator = '+'
                print(e)
                num2 = getNum("num2")
                break

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            try:
                divisionLogicCheck(num2, operator)
                result = num1 / num2
            except DivideByZero as e:
                print(e)
                result = num1

        print(f"Result: {result}")
        num1 = result

if __name__ == "__main__":
    try:
        main()
    except Exit as e:
        print(e)
        exit()