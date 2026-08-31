import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    available = [[] for _ in range(40)]
    stack = deque([(n, 0)]) # to divide
    visit = {n}
    while stack:
        cur, lvl = stack.pop()
        available[lvl].append(cur)
        if cur == 1: continue
        for nxt in [cur//2, (cur+1)//2]:
            if nxt not in visit:
                visit.add(nxt)
                stack.appendleft((nxt, lvl+1))
    flag = True
    for i in range(40):
        if k in set(available[i]):
            flag = False
            print(i)
            break
    if flag: print(-1)
        
    # 21 -> 10, 11 -> 5,6 -> 3,2 -> 1
    # 10 -> 5 -> 2, 3 -> 1