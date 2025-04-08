import random
import string

english_letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
list_english_and_symbols = english_letters + digits + symbols

password = []
len_password = random.randrange(12, 16)
for i in range(len_password):
    key = random.choice(list_english_and_symbols)
    password.append(key)

result = ''.join(password)
print(result)
