n = (int(input())) # 상담일수 입력
t = []
p = []
dynamic = [0] * (n+1) # 다이나믹 배열 초기화
max_val = 0 # 최대값을 0으로 초기화

for _ in range(n):
    time, price = map(int, input().split()) # 기간, 금액 입력
    t.append(time)
    p.append(price)

for i in range(n-1,-1,-1): # 뒤쪽부터 확인하면서
    if t[i] + i <= n: # 상담일수 안에 끝나게 되면
        dynamic[i] = max(p[i] + dynamic[t[i]+i], max_val) # 현재 이윤 + 상담을 마친 날짜로부터의 최대이윤을 더한값 , max 비교 최대값
    else:
        dynamic[i] = max_val
print(max_val)

