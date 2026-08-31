import sys
from collections import deque
input = sys.stdin.readline

def dfs(cy, cx):
    visit.add((cy,cx))
    stack = deque([(cy, cx)])
    lake_size = 0
    while stack:
        y, x = stack.pop()
        lake_size += field[y][x]
        
        for nx, ny in [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
            if 0 <= nx < m and 0 <= ny < n and (ny, nx) not in visit and field[ny][nx] != 0:
                visit.add((ny, nx))
                stack.append((ny, nx))
    
    return lake_size

for _ in range(int(input())):
    n, m = map(int, input().split())
    field = []
    for _ in range(n):
        field.append(list(map(int,input().split())))

    ans = 0
    visit = set()

    for y in range(n):
        for x in range(m):
            if (y,x) not in visit and field[y][x] != 0:
                ans = max(dfs(y, x), ans)
    print(ans)