n = int(input())
a = 0
b = 666
while True:
    if '666' in str(b):
        a += 1
    if a == n:
        print(b)
        break
    b += 1