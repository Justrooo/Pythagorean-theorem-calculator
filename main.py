from math import sqrt
from time import sleep


def write():
    print("Welcome to the Pythagorean theorem calculator v 1.0")
    sleep(1)
    print("Select one of the options:")
    sleep(1)
    print("1. You have a and b but you want to calculate c")
    print("2. You have a and c but you want to calculate b")
    print("3. You have b and c but you want to calculate a")
    print("4. Exit program")


def calc_a(b, c):
    print("")
    print(sqrt(c*c - b*b))
    print("")


def calc_b(a, c):
    print("")
    print(sqrt(c*c - a*a))
    print("")


def calc_c(a, b):
    print("")
    print(sqrt(a*a + b*b))
    print("")


while True:
    try:
        write()
        opt = int(input("Your choice: "))
        if opt == 1:
            calc_c(int(input("a: ")), int(input("b: ")))
            continue
        elif opt == 2:
            calc_b(int(input("a: ")), int(input("c: ")))
            continue
        elif opt == 3:
            calc_a(int(input("b: ")), int(input("c: ")))
            continue
        elif opt == 4:
            break
        else:
            sleep(1)
            print("")
            print("Type OPTION number from 1-4")
            print("")
            del opt
            sleep(1)
            write()
            opt = int(input("Your choice: "))
    except ValueError:
        sleep(1)
        print("")
        print("Please type a NUMBER")
        print("")
sleep(1)
print("Thank you for using my Pythagorean theorem calculator. Please report bugs at <GitHub Link>")
sleep(3)
input("Press any key to exit")
