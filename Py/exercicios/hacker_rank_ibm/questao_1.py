def play_segments(coins):
    n = len(coins)
    
    for i in range(n+1):
        player_1 = sum(coins[:i]) - (i - sum(coins[:i]))
        player_2 = sum(coins[i:]) - (n - i - sum(coins[i:]))
        
        if player_1 > player_2:
            return i
        
    return n


def playSegments(coins):
    n = len(coins)
    player_1_score = 0
    player_2_score = sum(coins) - (n - sum(coins))
    
    for i in range(n):
        if player_1_score > player_2_score:
            return i
        
        player_1_score += 2 * coins[i] - 1
        player_2_score -= 2 * coins[i] - 1
    
    return n