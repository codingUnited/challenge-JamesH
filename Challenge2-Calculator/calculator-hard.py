import ast
import math
import re

class OperationError(Exception):
    def __init__(self, message="Please select a valid operation (+, -, *, /): "):
        super().__init__(message)

def validate_input(value):
    if not all(char in set('0123456789+-/*^() sqrt√') for char in value):
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
    def __init__(self, message="Please don't try to divide by zero. \nResult unchanged."):
        super().__init__(message)

def divisionLogicCheck(value):
    if re.search(r"/\s*0", value):
        raise DivideByZero()

SAFE_FUNCTIONS = {

}

def main():
    print("Welcome to your calculator!")
    storage = 0
    
    # main loop
    while(True):
        prompt = f"{storage} " if storage != 0 else "Enter an expression: "
        expr = input(prompt)

        # make expression evaluable by python eval 
        try:
            clear_input(expr)
            exit_input(expr)
            validate_input(expr)
            divisionLogicCheck(expr)
            expr = expr.replace('^', '**')
            expr = expr.replace('sqrt', 'math.sqrt')
            expr = re.sub(r'√\(', r'math.sqrt(',expr)
            expr = re.sub(r'√([a-zA-Z0-9\.]+)', r'math.sqrt(\1)', expr)
            # () loop
            while(re.search(r'(?<!sqrt)\([^()]*\)', expr)):
                expr = re.sub(r'(?<!sqrt)\([^()]*\)', lambda expression: str(eval(expression.group())), expr)
            # if the expression does not start with an operator treat storage as 0
            if expr[0].isdigit() or expr[0] == 'm':
                storage = 0
            # add simplified expression to storage
            storage =  eval(expr, {"__builtins__": None}, {"math": math}) if storage == 0 else eval(str(storage) + expr, {"__builtins__": None}, {"math": math})
        except OperationError:
            print("Please enter a valid expression")
        except Clear: 
            storage = 0
        except DivideByZero as e:
            print(e)
        except Exit:
            raise
        except Exception as e:
            print(e)
         
    
    
    

if __name__ == "__main__":
    try:
        main()
    except Exit as e:
        print(e)
        exit()