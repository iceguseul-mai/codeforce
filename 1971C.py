def make_checklist1(start, end):
    i = start
    ans = []
    while i != end:
        ans.append(i)
        i = (i + 1) % 13 
    ans.append(i)
    return ans

def make_checklist2(start, end):
    i = start
    ans = []
    while i != end:
        ans.append(i)
        i -= 1
        if i == 0:
            i = 12
    ans.append(i)
    return ans

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    outer = make_checklist2(a, b)
    inter = make_checklist1(a, b)
    if (c in inter and d in inter) or (c in outer and d in outer):
        print("NO")
    else:
        print("YES")
    