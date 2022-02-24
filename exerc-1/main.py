def read_input(file: str) -> list[list[str]]:
    output = []
    with open(file) as f:
        for line in f:
            output.append(line.split())
    return output


if __name__ == '__main__':
    out = read_input("tests/a_an_example.in.txt")
