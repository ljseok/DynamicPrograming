d = [0] * 100 # 리스트 초기화
d[1] = 1 # 첫번재 항을 1로 설정
d[2] = 1 # 두번째 항을 1로 설정
n = 99 # 99번째 항

for i in range(3, n+1): # 3번째 항부터 n 번째 항까지 반복
    d[i] = d[i-1] + d[i-1]
print(d[n])