import socket

HOST = "127.0.0.1"
PORT = 5001


def connect_to_server():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        print("Connected to server.")
        return s
    except Exception as e:
        print(f"Connection failed: {e}")
        return None


def download_file(save_as="test.txt"):
    s = connect_to_server()
    if s is None:
        return

    try:
        s.sendall(b"DOWNLOAD")
        response = s.recv(1024)

        if response.startswith(b"ERR"):
            print("Server error:", response.decode())
            return

        print("Downloading file...")
        data = b""

        while True:
            packet = s.recv(1024)
            if not packet:
                break
            data += packet

        with open(save_as, "wb") as f:
            f.write(data)

        print(f"File downloaded successfully as '{save_as}'")

    except Exception as e:
        print("Error downloading file:", e)
    finally:
        s.close()
