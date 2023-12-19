def count(numbers):
    n = len(numbers)
    items = [1] * n

    for i in range(1, n):
        for j in range(i):
            if numbers[i] > numbers[j]:
                items[i] += items[j]

    return sum(items)

if __name__ == "__main__":
    print(count([1, 1, 2, 2, 3, 3])) # 26
    print(count([1, 1, 1, 1])) # 4
    print(count([5, 4, 3, 2, 1])) # 5
    print(count([4, 1, 5, 6, 3, 4, 1, 8])) # 37
    print(count([10])) #1
    print(count([4, 5])) #3