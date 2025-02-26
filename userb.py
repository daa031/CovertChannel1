import socket
import threading
import time

IP = '127.0.0.1'
PORTB = 6003

def userb():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s_b:
        s_b.bind((IP, PORTB))
        while True:
            data, _ = s_b.recvfrom(1024)
            print(f"UserB received: {data} with len {len(data)}")

if __name__ == "__main__":
    userb()