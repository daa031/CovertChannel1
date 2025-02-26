import socket
import threading
import time


IP = '127.0.0.1'
PORTA = 5001
PORTB = 6001
MSG = 'Hello from usera'
DELAY = 2
PATTERN = "Hello"

def fw():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_fw:
        s_fw.bind((IP, PORTA))
        s_fw.listen()
        while True:
            conn, _ = s_fw.accept()
            with conn:
                data = conn.recv(1024).decode()
                print("\n\n =============")
                print(f"FW received: {data}")
                print(f"length: {len(data)}")
                # keyword = PATTERN
                # if keyword in data:
                #     print(f"Keyword found: {keyword}")
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_fw_to_b:
                    s_fw_to_b.connect((IP, PORTB))
                    s_fw_to_b.sendall(data.encode())

if __name__ == "__main__":
    fw()