# This file was created to test out how argon2 password hasher works and how we can verify it.

from argon2 import PasswordHasher

password_hasher = PasswordHasher()

original_password = 'easy-password'
hashed_password = password_hasher.hash(original_password)

user_input_password = 'easy-password'

try:
    password_hasher.verify(hashed_password, user_input_password)
    print(type(hashed_password))
    print("success")
except:
    print('failed')