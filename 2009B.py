from collections import deque

t = int(input())

for _ in range(t):
    ans = deque()
    for _ in range(int(input())):
        s = input()
        if s[0] == '#':
            ans.appendleft(1)
        elif s[1] == '#':
            ans.appendleft(2)
        elif s[2] == '#':
            ans.appendleft(3)
        elif s[3] == '#':
            ans.appendleft(4)
    print(*ans)