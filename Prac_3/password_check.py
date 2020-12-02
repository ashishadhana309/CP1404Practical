MIN_LENGTH = 2
MAX_LENGTH = 10


def main():
    password = input("Password > ")
    while not check_length(password):
        print("Password must be between {0} and {1}".format(MIN_LENGTH, MAX_LENGTH))
        password = input("Password > ")
    for character in range(0, check_length(password)):
        print("*", end=' ')


def check_length(password):
    pass_length = len(password)
    if pass_length < MIN_LENGTH or pass_length > MAX_LENGTH:
        return False
    else:
        return pass_length


main()
