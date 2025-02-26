import socket
import threading
import time

import random
import string

IP = '127.0.0.1'
PORTA = 5004
PORTB = 6004
MSG = 'DAA031@\n'
DELAY = 2
N = 2


def calculate_range(char, n):
    ascii_code = ord(char)
    lower_bound = (ascii_code - 1) * N
    upper_bound = ascii_code * n
    return lower_bound, upper_bound

def send(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_fw_to_b:
        print(f"FW send: {data}\n")
        s_fw_to_b.connect((IP, PORTB))
        s_fw_to_b.sendall(data.encode())


def fw(msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_fw:
        s_fw.bind((IP, PORTA))
        s_fw.listen()
        while True:
            conn, _ = s_fw.accept()
            with conn:
                packet = conn.recv(1024).decode()
                length = len(packet)
                print(f"FW received: {packet} | length: {length}")
                while True:
                    if not msg:
                        break 

                    symbol = msg.pop(0) 
                    lower, upper = calculate_range(symbol, N)  
                    if lower < length <= upper:
                        send(packet) 
                        break 

                    elif length < lower:
                        packet = packet + "X" * (upper - length)
                        #packet = packet + ''.join(random.choices(string.ascii_letters + string.digits, k=(upper - length)))
                        send(packet)
                        break  

                    else:
                        send(packet[:upper])
                        packet = packet[-(length - upper):]
                        break 
if __name__ == "__main__":
    msg = list(MSG)
    fw(msg)

