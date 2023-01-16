test_case = int(input())
ans = []
for case in range(test_case):
    num_of_document, wanted = map(int, input().split())
    priority_list = list(map(int, input().split()))
    count = 1
    while wanted >= 0:
        if wanted != 0:
            if priority_list[0] < max(priority_list):
                priority_list = priority_list[1:] + priority_list[:1]
                wanted -= 1
            elif priority_list[0] == max(priority_list):
                priority_list.pop(0)
                wanted -= 1
                count += 1
        else:
            if priority_list[0] < max(priority_list):
                priority_list = priority_list[1:] + priority_list[:1]
                wanted = len(priority_list) - 1 
            elif priority_list[0] == max(priority_list):
                wanted -= 1
                break
    print(count)