from typing import Literal
def perform_operation(num1 : float , num2 : float , operation:Literal['add','subtract','multiply','divide'] ):
    if operation == "add" :
        return num1 + num2
    elif operation == "multiply" :
        return num1 * num2
    elif operation == "divide" :
         if num2 != 0 :
             return num1 / num2 
    elif operation == "subtract" :
        return num1 - num2
    else :
        return "Invalid operation"  # Return a message if the operation is not recognized
    



