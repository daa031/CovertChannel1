import socket
import threading
import time

IP = '127.0.0.1'
PORTB = 6004
N = 2

def hacker(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_b:
        s_b.bind((IP, PORTB))
        s_b.listen()
        while True:
            conn, _ = s_b.accept()
            with conn:
                packet = conn.recv(1024).decode()
                code_ascii = len(packet) // N  
                if code_ascii == 9:
                    print("Message was delivered")
                    return
                # print(f"{chr(code_ascii)} | {len(packet)}")
                data += chr(code_ascii)
                print(f'received packet: {packet}\nCovert msg:{data}\n==========')

if __name__ == "__main__":
    data = ''
    hacker(data)