import sys
input = sys.stdin.readline

for _ in range(int(input())):
    score = 0
    n = int(input())
    a = sorted(list(map(int, input().split())))
    print(a.count(0) + sum(a))

