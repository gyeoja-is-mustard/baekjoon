n = int(input())
set = set()
res = []
for i in range(n):
    set.add(input())
list = list(set)
a = list
index = []
for j in range(len(a)):
    b = a[j]
    a[j] = a[j].upper()
    for k in range(len(a[j])):
        b = str(ord(a[j][len(a[j])-k-1])) + b
    c = b.replace(a[j].lower(), '0')
    a[j] = int(c)
a.sort()
d =''
for l in range(len(a)):
    a[l] = str(a[l])
    for m in range(0, int((len(a[l])-1)/2)):
         d += chr(int(a[l][2*m]+a[l][2*m+1])).lower()
    res.append(d)
    d = ''
for n in range(len(res)):
    print(res[n])