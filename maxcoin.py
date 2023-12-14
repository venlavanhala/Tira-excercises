
def min_coins(x, coins):
    result = {}
    
    result[0] = 0
    for s in range(1, x + 1):
        result[s] = float("inf")
        for coin in coins:
            if s - coin >= 0:
                result[s] = min(result[s], result[s - coin] + 1)
        print(result)

    return result[x]

def find(x, coins):
    result = {}
    
    result[0] = 0
    for s in range(1, x + 1):
        result[s] = -1
        for coin in coins:
            if s - coin >= 0:
                if result[s-coin] > -1:
                    result[s] = max(result[s], result[s - coin] + 1)
                    #print(f"s: {s}, coins: {coin}, result[s]: {result[s]}, result[s-coins]: {result[s-coin]}")
    #print(result)

  #  pairs = 0
  #  for coin in coins:
  #      if coin % 2 == 0:
  #          pairs += 1
  #  if pairs == len(coins) and x % 2 != 0:
  #      return -1
    return result[x]

def find2(x, coins):
    result = {}
    result[0] = 0


if __name__ == "__main__":
    print(find(13, [1, 2, 5])) # 13
    print(find(13, [2, 3, 5])) # 6
    #print(find(13, [3,5,6]))
    print(find(13, [2, 4, 6])) # -1
    print(find(42, [8, 9, 11, 15])) # 5
