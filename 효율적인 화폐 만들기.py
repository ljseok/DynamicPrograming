n,m = map(int,input().split()) # 화폐의 단위 갯수 , 돈 입력받기
arr = []

for i in range(n):
    arr.append(int(input())) # 화폐의 단위 입력받기

d = [10001] * (m+1) # 최대갯수가 10000이므로 그 보다 1큰값으로 초기화
d[0] = 0

for i in range(n): # 화폐단위를 확인
    for j in range(arr[i], m+1): # 금액을 확인
        if d[j - arr[i]] != 10001: # 금액에서 화폐단위를 뺀 값이 존재할 경우
            d[j] = min(d[j], d[j - arr[i]] + 1)

if d[m] == 10001: # 방법이 존재하지 않는 경우
    print(-1)
else: # 방법이 존재하는 경우
    print(d[m])