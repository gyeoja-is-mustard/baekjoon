N= int(input())
N_list = list(map(int, input().split()))
N_dic = {N_list[j]:1 for j in range(N)}
M = int(input())
M_list = list(map(int, input().split()))
for j in range(M):
    if M_list[j] in N_dic:
        print(1)
    else:
        print(0)