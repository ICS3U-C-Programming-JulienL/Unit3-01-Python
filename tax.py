#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: October 10, 2023
# This program calculates the tax and total using the subtotal
import constants


def main():
    # get the subtotal
    print("Calculating the Tax and Total using the Subtotal")
    subtotal = float(input("What is the subtotal of your item in dollars?"))

    # calculate tax and total cost
    tax = constants.HST * subtotal
    total = subtotal + tax

    # display the tax and the total cost
    print("Your tax is ${:.2f}.".format(tax))
    print("Your total cost is ${:.2f}.".format(total))


if __name__ == "__main__":
    main()
