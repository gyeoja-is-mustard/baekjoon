x = int(input())
y = int(input())
if x > 0:
    if x * y < 0:
        print('4')
    else:
        print('1')
else:
    if x * y < 0:
        print('2')
    else:
        print('3')