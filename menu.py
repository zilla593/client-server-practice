
import client
import edit


def main_menu():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Connect to server")
        print("2. Download file from server")
        print("3. Edit downloaded file")
        print("0. Exit")
        choice = input("Enter option: ").strip()

        if choice == "1":
            client.connect_to_server()
        elif choice == "2":
            try:
                client.download_file("test.txt")
            except Exception:
                print("Not connected or download failed.")
        elif choice == "3":
            filename = input("Enter filename: ").strip() or "test.txt"
            edit.edit_file(filename)
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main_menu()
