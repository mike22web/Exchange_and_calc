n, k = int(input()), int(input())
lst = list(range(1, n+1))
while len(lst) > 1:
    if k < len(lst)-1:
        del lst[k]
        for i in range(k):
            lst.append(lst[i])
        del lst[:k]
    else:
        k -= len(lst)
        del lst[k]
        for i in range(k):
            lst.append(lst[i])
        del lst[:k]













print(lst)