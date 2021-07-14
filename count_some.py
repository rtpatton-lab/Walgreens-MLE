def count_some(starting_num, ending_num, k):
    lst = []
    if (starting_num == ending_num):
        lst.append(starting_num)
    else:
        while (starting_num < ending_num + 1):
            lst.append(starting_num)
            starting_num += 1

    counter = 0
    n = len(lst)
    for i in range(0, n, 1):
        if (lst[i] % k == 0):
            counter += 1

    return counter

if __name__ == '__main__':
    starting_num = 0
    ending_num = 10
    k = 5

    print(count_some(starting_num, ending_num, k))






    