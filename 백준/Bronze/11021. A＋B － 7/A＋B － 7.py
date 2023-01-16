T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    C = A + B
    print('Case #%d: %d' % (i+1, C))