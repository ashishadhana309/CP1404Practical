def main():
    number = False
    while not number:
        try:
            score = int(input("Score > "))
            number = True
            print(result(score))
        except ValueError:
            print("Only number accepted")


def result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif 85 <= score <= 100:
        return "HD"
    elif 75 <= score < 85:
        return "D"
    elif 65 <= score < 75:
        return "C"
    elif 50 <= score < 65:
        return "P"
    else:
        return "F"


main()
