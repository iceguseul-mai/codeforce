import sys
input = sys.stdin.readline

# def search(origin, cur):
#     if cur == origin: return True
#     visit[cur] = 1
#     if cur + x <= n and visit[cur+x] == 0:
#         if search(origin, cur + x): return True
#     if cur + y <= n and visit[cur+y] == 0:
#         if search(origin, cur + y): return True
#     if cur - x >= 1 and visit[cur-x] == 0:
#         if search(origin, cur - x): return True
#     if cur - y >= 1 and visit[cur-y] == 0:
#         if search(origin, cur - y): return True
#     return False

for _ in range(int(input())):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    comp = [-1] * (n + 1)
    cnt = 0
    for i in range(1, n + 1):
        cnt += 1
        if comp[i] != -1:
            continue
        stack = [i]
        comp[i] = cnt
        while stack:
            cur = stack.pop()
            for nxt in [cur + x, cur - x, cur + y, cur - y]:
                if 1 <= nxt <= n and comp[nxt] == -1:
                    comp[nxt] = cnt
                    stack.append(nxt)
    flag = 0
    for i in range(1, n+1):
        if comp[i] != comp[a[i]]:
            flag = 1
            break
    print("NO" if flag else "YES")