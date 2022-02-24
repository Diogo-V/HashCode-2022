def read_input(file: str) -> None:
    with open(file) as f:
        for line in f:
            out = line.split()
            print(out)


if __name__ == '__main__':
    read_input("tests/a_an_example.in.txt")
