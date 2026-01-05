def edit_file(filename):
    try:
        with open(filename, "r", newline='') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: File not found.")
        return

    if not lines:
        print("File is empty.")
        return

    while True:
        print("\n" + "=" * 40)
        for i, line in enumerate(lines, 1):
            print(f"{i:3}: {line.rstrip()}")
        print("=" * 40)

        try:
            num = input("\nLine number to edit (0 to save & exit): ").strip()
            if num == "0":
                break
            line_number = int(num)
        except ValueError:
            print("Enter a valid number.")
            continue

        if not 1 <= line_number <= len(lines):
            print("Out of range.")
            continue

        new_text = input("New text: ")
        lines[line_number - 1] = new_text + "\n"

        with open(filename, "w", newline='') as f:
            f.writelines(lines)

        print("File saved.")

