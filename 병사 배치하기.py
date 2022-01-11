n = int(input())
arr = list(map(int,input().split()))
arr.reverse()

Dynamic = [1] * n
for i in range(1,n):
    for j in range(0,i):
        if arr[j] < arr[i]:
            Dynamic[i] = max(Dynamic[i], Dynamic[j]+1)

print(n-max(Dynamic))