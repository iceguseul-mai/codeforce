import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    seq = deque(list(input().rstrip()))
    x, y = 0, 0
    flag = True
    for _ in range(100):
        for c in seq:
            if "N" == c:
                y += 1
            if "S" == c:
                y -= 1
            if "W" == c:
                x -= 1
            if "E" == c:
                x += 1
            if (x,y) == (a,b):
                print("YES")
                flag = False
                break
        if not flag:
            break
    if flag:
        print("NO")