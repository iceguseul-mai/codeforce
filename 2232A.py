import sys
from collections import deque
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    a = deque(sorted(list(map(int, input().split()))))
    cnt = 0
    while len(set(a)) > 1:
        a.pop()
        a.popleft()
        cnt += 1
    print(cnt)