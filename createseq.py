def find(items):
    result = [0] * len(items) #lista pituuksista
    best = {}

    for i in range(len(items)):
        result[i] = 1
        for j in range(i):
            if items[j] < items[i]:
                result[i] = max(result[i], result[j] + 1)
                print(f"result[i]: {result[i]}")
                print(f"i: {i}, j: {j}")
                if j in best.keys():
                    best[items[j]].append(items[i])
                else:
                    best[items[j]]=[items[i]]

    return best

def find2(items):
    best = {}

    for i in range(len(items)):
        for j in range(i, len(items)):
            if items[i] < items[j]:
              #  print(f"i: {i}, j: {j}")
                if i in best.keys():
                    best[i].append(j)
                else:
                    best[i]=[j]

    print(best)
    # best on sellainen kuin pitäisikin

    if not best:
        return items[0]

    all = []

    for key in best.keys():
        new_list = []
        new_list.append(items[key])
        for number in best[key]:
            new_list.append(items[number])
        print(new_list)
        if new_list == sorted(new_list):
            all.append(new_list)

    print(all)
    return max(all, key=len)

    """
    newbest = []
    #print(f"best: {best}")
    for i in best.keys(): # Lisätään listaan aina bestin avain ja arvot
        newlist = [items[i]] + [items[best[i][j]] for j in range(len(best[i]))]
        newlist = set(newlist)
        if newlist == sorted(newlist):
            newbest.append(newlist)
            print(newbest)
    if newbest:
        return newbest
    else:
        return items[0]

        """

if __name__ == "__main__":
    print(find2([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find2([1, 1, 1, 1])) # [1]
    print(find2([5, 4, 3, 2, 1])) # [3]
    print(find2([4, 1, 5, 6, 3, 4, 1, 8])) # [1, 3, 4, 8]

