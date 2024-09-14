from sys import stdin

n, p = map(int, stdin.readline().split())
visited = [n]
last = n
while True:
    cur = last * n % p
    for i in range(len(visited)):
        if visited[i] == cur:
            print(len(visited) - i)
            exit()
    visited.append(cur)
    last = cur
