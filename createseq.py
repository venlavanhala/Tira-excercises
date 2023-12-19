def find(items):
    numbers = [1] * len(items)
    prev_index = [-1] * len(items)
    max_length = 0
    max_index = 0
    for i in range(len(items)):
        for j in range(i):
            if items[i] > items[j] and numbers[i] < numbers[j] + 1:
                numbers[i] = numbers[j] + 1
                prev_index[i] = j

        if max_length < numbers[i]:
            max_length = numbers[i]
            max_index = i
    lis = []
    while max_index != -1:
        lis.append(items[max_index])
        max_index = prev_index[max_index]

    return lis[::-1]

if __name__ == "__main__":
    print(find([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find([1, 1, 1, 1])) # [1]
    print(find([5, 4, 3, 2, 1])) # [3]
    print(find([4, 1, 5, 6, 3, 4, 1, 8])) # [1, 3, 4, 8]
    print(find([9, 6, 10, 10, 3, 6, 7, 6, 5, 7]))