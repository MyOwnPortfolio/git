li = [9, 5, 10, -1, 7, 0, 2, 4, 6, 3, 1, -3, 4.5, 8, -8, -6]
n = 1
while n < len(li):
    for i in range(len(li)-n):
        if li[i] > li[i + 1]:
            li[i], li[i + 1] = li[i + 1], li[i]
    n += 1
print(li)
