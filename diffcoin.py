def count(x, coins):
    result = {}
    
    result[0] = 1
    for s in range(1, x + 1):
        result[s] = 0
        for coin in coins:
            if s - coin >= 0:
                result[s] += result[s - coin]
                
    return result[x]

if __name__ == "__main__":
    print(count(5, [1])) # 1
    print(count(5, [1, 2])) # 3
    print(count(13, [1, 2, 5])) # 14
    print(count(42, [1, 5, 6, 17])) # 58
    print(count(99, [2, 4, 6])) # 0