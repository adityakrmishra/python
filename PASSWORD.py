import socket
import re
import sys

def connect(username, password):
    sample = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sample.connect(('localhost', 9999))
    sample.sendall(f'{username},{password}'.encode())
    response = sample.recv(1024).decode()
    sample.close()
    return response

def validate_username(username):
    return re.match("^[a-zA-Z0-9_]+$", username)

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*()_+-=]", password):
        return False
    return True

def main():
    username = input("Enter username: ")
    if not validate_username(username):
        print("Invalid username. Only letters, numbers, and underscores are allowed.")
        sys.exit(1)

    password = input("Enter password: ")
    if not validate_password(password):
        print("Invalid password. Password must be at least 8 characters long, contain a mix of upper and lower case letters, numbers, and special characters.")
        sys.exit(1)

    response = connect(username, password)
    print("Server response:", response)

if __name__ == "__main__":
    main()
