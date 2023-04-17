import sys 
import logger
import logging

def error_message_details(error, error_detail:sys):
    '''
     exc_info() returns the tuple (type(e), e, e.__traceback__). 
     That is, a tuple containing the type of the exception (a subclass of BaseException), 
     the exception itself, 
     and a traceback object which typically encapsulates the call stack at the point where the exception last occurred
     file of error, line of error and all the details.
    '''
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_mess = str(error)
    error_message = 'Error occured in the python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name, line_number, error_mess
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message


        