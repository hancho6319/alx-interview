def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize dp array where dp[i] will store the fewest coins needed to make the amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins are needed to make 0
    
    # Iterate through each coin
    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still infinity, return -1 (not possible to make total)
    return dp[total] if dp[total] != float('inf') else -1

