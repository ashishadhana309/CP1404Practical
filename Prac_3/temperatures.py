def main():

    celc = False
    while not celc:
        try:
            celsius = float(input("Celsius > "))
            celc = True
            print("{0} celsius = {1:.2f} fahrenheit".format(celsius, celsius_to_fahrenheit(celsius)))
        except ValueError:
            print("Only number accepted")

    fahr = False
    while not fahr:
        try:
            fahrenheit = float(input("Fahrenheit > "))
            fahr = True
            print("{0} fahrenheit = {1:.2f} celsius".format(fahrenheit, fahrenheit_to_celsius(fahrenheit)))
        except ValueError:
            print("Only number accepted")


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius


main()
