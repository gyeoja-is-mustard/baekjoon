A = int(input())
B = int(input())
C = int(input())
D = A*B*C
E = str(D)
for i in range(10):
    print(E.count('%d' % i))