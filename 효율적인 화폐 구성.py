'''
n,m = map(int,input().split()) # 정수 n,m 입력 받기 n = 화폐 종류 , m = 화폐들의 합

array=[]

for i in range(n):
    array.append(int(input))
'''
n = 3
m = 4
array = [(3),(5),(7)]
d = [10001] * (m+1) # 테이블 초기화

# 동적 프로그래밍

d[0] = 0
for i in range(n): # i는 화폐단위
    for j in range(array[i], m+1):
        if d[j -array[i]] != 10001: # (i-k)원을 만드는 방법이 존재할 경우
            d[j] = min(d[i], d[j-array[i]] +1)

# 결과 출력

if d[m] == 10001: # (i-k)원을 만드는 방법이 없을 경우
    print(-1)
else: # 존재하는 경우
    print(d[m])

