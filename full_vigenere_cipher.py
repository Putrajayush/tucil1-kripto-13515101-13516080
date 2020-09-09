import random
import string

def key_generator(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(26))
    print(result_str)

