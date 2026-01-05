
import socket
import os

HOST = "127.0.0.1"
PORT = 5001
FILE_NAME = "test.txt"


def send_file(conn):
    if not os.path.exists(FILE_NAME):
        conn.sendall(b"ERROR")
        return

    file_size = os.path.getsize(FILE_NAME)
    conn.sendall(f"OK {file_size}".encode())

    with open(FILE_NAME, "rb") as f:
        while chunk := f.read(4096):
            conn.sendall(chunk)
    print("File sent.")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {PORT}...")

        while True:
            conn, addr = s.accept()
            print(f"Client connected: {addr}")
            try:
                if conn.recv(1024).decode().strip() == "DOWNLOAD":
                    send_file(conn)
            except Exception as e:
                print("Error:", e)
            finally:
                conn.close()


if __name__ == "__main__":
    main()
