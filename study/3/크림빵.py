n, k, p = map(int, input().split())
bread = [int(x) for x in input().split()]
ans = 0

for i in range(n):
    curr_p = 0
    flag = False
    for j in range(k):
        if curr_p >= p:
            flag = True
            break
        if bread[i * k + j] == 0:
            curr_p += 1
            if curr_p >= p:
                flag = True
                break
    if flag == False:
        ans += 1

print(ans)
