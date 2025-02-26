import socket
import threading
import time
import random
import string

IP = '127.0.0.1'
PORT = 5004
DELAY = 1
MAX_LENGTH = 256 

def generate_random_message(max_length):
    length = random.randint(1, max_length)
    return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=length))

def usera():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((IP, PORT))
            message = generate_random_message(MAX_LENGTH)
            print(f'send message: {message}\n')
            s.sendall(message.encode())
        time.sleep(DELAY)

if __name__ == "__main__":
    usera()
