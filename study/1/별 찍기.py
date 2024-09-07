n = int(input())
for i in range(n):
    if i < n:
        print(" " * (n - i - 1), end="")
    print("*" * (i * 2 + 1))
for j in range(n - 2, -1, -1):
    print(" " * (n - j - 1), end="")
    print("*" * (j * 2 + 1))
