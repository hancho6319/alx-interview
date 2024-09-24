def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total >= coin:
            num_coins += total // coin
            total %= coin
        if total == 0:
            return num_coins

    return -1

