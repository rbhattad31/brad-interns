class CustomException(Exception):
    """ my custom exception class """


try:
    raise CustomException('This is my Custom exception')
except CustomException as ex:
    print(ex)
