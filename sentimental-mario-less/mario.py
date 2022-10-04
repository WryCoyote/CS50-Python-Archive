# TODO
from cs50 import get_int


def main():
    while (True):
        # get height
        height = get_int("Height: ")
        # check height
        if height > 0 and height < 9:
            pyramid(height)
            break
        else:
            print("Not a valid value, try again!")


def pyramid(height):
    # build pyramid
    for i in range(height):
        print(" " * (height - i - 1), end="")
        print("#" * (i + 1), end="\n")


if __name__ == "__main__":
    main()