def main() -> None:
    name = input("Enter name of the file: ")
    lines = ""
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines += line + "\n"
    with open(f"{name}.txt", "w") as f:
        f.write(lines)


if __name__ == "__main__":
    main()
