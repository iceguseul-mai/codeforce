import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n,m = map(int, input().split())
    stack = deque([m])
    visit = set()
    flag = False

    if n < m or (n % 3 != 0 and n!=m):
        print("NO")
        continue

    while stack:
        cur = stack.popleft()
        visit.add(cur)
        if cur > n:
            continue
        if cur == n:
            flag = True
            print("YES")
            break
        if cur % 2 == 0 and cur*1.5 not in visit:
            stack.append(cur*1.5)
        if cur*3 not in visit:
            stack.append(cur*3)
    
    if not flag:
        print("NO")

    