#%%
def verify_passw(password):
    conn = sqlite3.connect('hash_password.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM passwords')
    items = cur.fetchall()
    for _ in items:
        password += _[1]
        password = password.encode()
        password = hashlib.sha256(password).hexdigest()
        if password == _[0]:
            return True
        else:
            return False


#%%
# Imports:
import random
import string
import hashlib
import sqlite3

# Initialization of password variables
password = ''
check_password = ''
PASSWORD_LENGTH_TO_CHANGE = 1


# Simple password validation
while (password != check_password) or len(password) < PASSWORD_LENGTH_TO_CHANGE:
    password = input(print('Podaj hasło:'))

    check_password = input(print('Powtórz proszę swoje hasło:'))

    if password != check_password:
        print('Wprowadzono różne hasła!')
    elif len(password) < PASSWORD_LENGTH_TO_CHANGE:
        print('Hasło musi zawierać conamniej 8 znaków!')

# Create the salt
salt = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
salt = 'xxxxx'


# Hashing salted password
print(password)
password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000).hex()
print('Brawo:',password)


# Connect to database
conn = sqlite3.connect('hash_password.db')

# Create a cursor
cursor = conn.cursor()

# # Create a table
# cursor.execute(
#     """CREATE TABLE passwords (
#         password text,
#         salt text
#         )"""
#     )

# # Commit the command
# conn.commit()

# Insert new data
cursor.execute("INSERT INTO passwords VALUES (?,?)", [password, salt])

# Commit the command
conn.commit()

# Get data from database
cursor.execute("SELECT * FROM passwords")

items = cursor.fetchall()

#for _ in items:
#    print(_[0])

# Close connection
conn.close()

# Password verification
if verify_passw('noga11'):
    print('Podane hasło jest poprawne!')
# %%
