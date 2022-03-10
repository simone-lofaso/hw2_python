def sort_list(l):
    n = len(l)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if l[j] > l[j + 1]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
            j += 1
        i += 1
    return l

print(sort_list([1, 3, 2, 7]))
print(sort_list([3, 2, 4, 89]))


            