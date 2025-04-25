# User-defined exception
class PasswordError(Exception):
    pass

# Main program
try:
    password = input("Enter your password: ")
    if password != "hello123":
        raise PasswordError
    print("Password is correct!")
except PasswordError:
    print("Wrong password!")
