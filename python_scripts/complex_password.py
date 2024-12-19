import string
from random import choices
import pyperclip

def create_password(length = 8, upper= False, lower=False, digit=False, pun= False):
    pool = ''
    if upper == True:
        pool += string.ascii_uppercase
    if lower == True:
        pool += string.ascii_lowercase
    if digit == True:
        pool += string.digits
    if pun == True:
        pool += string.punctuation
    if pool  == '':
        pool = string.ascii_lowercase
    result = ''.join(choices(pool, k=length))
    pyperclip.copy(result)
    return result
create_password(12, upper= True, lower=True, digit=True, pun= True)

# 9     1001