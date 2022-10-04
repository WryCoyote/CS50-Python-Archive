# TODO
from cs50 import get_float


def main():

    while (True):
        change = get_float("Change owed: ")
        if change >= 0.0:
            # print("change owed: ", change)
            change = change * 100

            quarters = int(change / 25)
            change = change - (quarters * 25)
            # print("quarters: ", quarters)
            # print("chgange: ", change)

            dimes = int(change / 10)
            change = change - (dimes * 10)
            # print("dimes: ", dimes)

            nickles = int(change / 5)
            change = change - (nickles * 5)
            # print("nickles: ", nickles)

            pennies = int(change / 1)
            change = change - (pennies * 1)
            # print("pennies: ", pennies)

            coins = quarters + dimes + nickles + pennies
            # print("coins: ", coins)
            # coins = coins / 100
            # print("coins1: ", coins)
            # coins = round(coins, 0)
            print(coins)
            break
        else:
            print("Invaild Input, try again!")


if __name__ == "__main__":
    main()