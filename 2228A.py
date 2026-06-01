import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt1 = a.count(1)
    cnt2 = a.count(2)
    cnt0 = a.count(0)

    pair = min(cnt1, cnt2)
    ans = cnt0 + pair
    cnt1 -= pair
    cnt2 -= pair

    print(ans + cnt1 // 3 + cnt2 // 3)