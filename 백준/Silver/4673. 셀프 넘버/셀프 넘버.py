list = list(range(10000))
def d(n):
    result = n
    a = str(n)
    for i in range(len(a)):
        result += int(a[i])
    return result
for i in range(10000):
    if d(i) in list:
        list.remove(d(i))
for j in list:
    print(j)
    