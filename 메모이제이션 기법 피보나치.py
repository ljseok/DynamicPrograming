d = [0] * 100 # 리스트를 초기화

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0: # 이미 계산을 했으면
        return d[x] # 그대로 반환
    d[x] = fibo(x-1) + fibo(x-2) # 계산하지 않았다면 피보나치 수열
    return d[x]
print(fibo(99))
