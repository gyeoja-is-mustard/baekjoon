a = list(map(int, input().split()))
b = [1, 2, 3, 4, 5, 6, 7, 8]
if a == b:
    print('ascending')
elif a == b[::-1]:
    print('descending')
else:
    print('mixed')