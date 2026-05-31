import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    frosting = list(map(int,input().split()))
    frosting.append(0)
    ans = [frosting[0]]
    cur = 0
    for i in range(n):
        # 2 2 5 3 2
        # ans =  
        if i == n-1:
            continue
        if frosting[i] < frosting[i+1]:
            ans.append(frosting[i])
            frosting[i+2] += (frosting[i+1]-frosting[i])
            frosting[i+1] = frosting[i]
        elif frosting[i] > frosting[i+1]:
            ans.append(round((frosting[i]+frosting[i+1])/2))
            avg = round((frosting[i]+frosting[i+1])/2)
            frosting[i] -= avg
            frosting[i+1] += avg
        else:
            ans.append(frosting[i])
    print(*ans)

# if [i] < [i+1] => i로 자르기 (min)
# if [i] > [i+1] => [i]와 [i+1]의 평균 (소숫점 없앰)