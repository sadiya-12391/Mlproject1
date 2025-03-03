import sys
import os
import logging
from src.logger import logging 

def error_message_detail(error, error_detail: sys):
    _, _,exc_tb = error_detail.exc_info()  # Get exception traceback first two are not important here 
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Correct usage of super()
        self.error_message = error_message_detail(error_message, error_detail=error_detail)  # Store detailed error message

    def __str__(self):
        return self.error_message

if __name__ == '__main__':
    try:
        a = 1 / 0  # Deliberate ZeroDivisionError
    except Exception as e:  # Catch the exception
        logging.basicConfig(level=logging.INFO)  # Set up basic logging
        logging.error(f"An exception occurred: {e}")  # Log the error
        raise CustomException(str(e), sys)  # Raise CustomException with error details
 