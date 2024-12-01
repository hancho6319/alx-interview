#!/usr/bin/python3
""" 0x08. Making Change """


def makeChange(coins, total):
    """ Return: fewest number of coins needed to meet total """
    if total <= 0:
        return 0

    """ To sort the coins in reverse """
    coins.sort(reverse=True)
    number_of_changes = 0
    total_changes = 0

    for coin in coins:
        while total_changes < total:
            total_changes += coin
            number_of_changes += 1

        if total_changes == total:
            return total_changes

        total_changes -= coin
        number_of_changes -= 1

    return -1
