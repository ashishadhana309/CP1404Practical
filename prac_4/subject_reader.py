FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():

    input_file = open(FILENAME)
    for line in input_file:
        print(line)
        print(repr(line))
        line = line.strip()
        parts = line.split(',')
        print(parts)
        parts[2] = int(parts[2])
        print(parts)
        print("----------")
    input_file.close()


main()