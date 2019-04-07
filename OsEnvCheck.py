import os

name = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASS')

print(name)
print(password)
