result1 = {}

def count_sequences1(n):
    if n == 0:
        return 1
    if n in result:
        return result[n]
    count = 0
    for i in range(2, n + 1, 2): #lisätään kaksi
        count += count_sequences1(i - 2) * count_sequences1(n - i)
    result[n] = count
    return count

result = {}
def count_sequences(n):
    count = 0
    for i in range(2, n+1, 2):
        if n == 0:
            return 1
        if n in result:
            return result[n]
        count = count + i-2 + n-i

    result[n] = count
    return count

print(count_sequences(100))
print(count_sequences1(100))