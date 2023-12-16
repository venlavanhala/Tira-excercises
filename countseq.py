# Montako nousevaa alijonoa?

def count(items):
    result = 0

    for i in range(len(items)):
        for j in range(i):
            if items[j] < items[i]:
                result += 1
    
    return result

def count3(x, coins):
    result = {}
    
    result[0] = 1
    for s in range(1, x + 1):
        result[s] = 0
        for coin in coins:
            if s - coin >= 0:
                result[s] += result[s - coin]
                
    return result[x]

def count1(numbers):
    result = {}
    
    result[0] = 1
    for s in range(1, x + 1):
        result[s] = 0
        for coin in coins:
            if s - coin >= 0:
                result[s] += result[s - coin]
                
    return result[x]

if __name__ == "__main__":
    print(count([1, 1, 2, 2, 3, 3])) # 26
    print(count([1, 1, 1, 1])) # 4
    print(count([5, 4, 3, 2, 1])) # 5
    print(count([4, 1, 5, 6, 3, 4, 1, 8])) # 37