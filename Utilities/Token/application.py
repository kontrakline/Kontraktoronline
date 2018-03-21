import logging
import json
from Controller import TokenController

def lambda_handler(pParam):
    token = TokenController.generateToken()

    print(token)
    print(TokenController.extractToken(token))
    return "asdasd"


if __name__ == "__main__" :
    lambda_handler("")