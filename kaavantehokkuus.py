import math
import time

# Sulkulausekekaava

def count_sequences(n):
    binom = (math.factorial(n)) / (math.factorial(int(n/2)) * math.factorial(int(n/2)))
    count = binom * (1 / (1 + n/2))
    return count

result1 = {}

def count_sequences1(n, d=0):
    if d < 0 or d > n:
        return 0
    if n == 0:
        return 1
    if (n, d) in result1:
        return result1[(n, d)]
    result1[(n, d)] = count_sequences1(n - 1, d + 1) + \
                     count_sequences1(n - 1, d - 1)
    return result1[(n, d)]

result2 = {}

def count_sequences2(n):
    if n == 0:
        return 1
    if n in result2:
        return result2[n]
    count = 0
    for i in range(2, n + 1, 2):
        count += count_sequences2(i - 2) * count_sequences2(n - i)
    result2[n] = count
    return count


start = time.time()
print(count_sequences(100))
middle = time.time()
print(count_sequences1(100))
middle2 = time.time()
print(count_sequences2(100))
end = time.time()
print(f"first: {middle-start}")
print(f"second: {middle2-middle}")
print(f"last: {end-middle2}")

start = time.time()
print(count_sequences(300))
middle = time.time()
print(count_sequences1(300))
middle2 = time.time()
print(count_sequences2(300))
end = time.time()
print(f"first: {middle-start}")
print(f"second: {middle2-middle}")
print(f"last: {end-middle2}")