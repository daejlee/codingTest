from sys import stdin

hr, min = map(int, stdin.readline().split())
cook = int(stdin.readline())
res = min + cook
if res < 60:
    print(hr, res)
else:
    n_hr = hr + res // 60
    n_min = res % 60
    if n_hr > 23:
        n_hr = n_hr % 24
    print(n_hr, n_min)
