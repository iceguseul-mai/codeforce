import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    cnt = 1
    i = 1
    while cnt < n:
        cnt = cnt * 2 + 2
        i += 1
    print(i)