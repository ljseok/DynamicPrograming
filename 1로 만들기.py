# x = int(input())  정수 X 입력
x = 26

d = [0] * 30001 # 테이블 초기화

# 동적 프로그래밍

for i in range(2, x+1):
    d[i] = d[i-1] + 1

    if i % 2 == 0: # 2로 나누어 떨어질 경우
        d[i] = min(d[i], d[i // 2] +1)

    if i % 3 == 0: # 3으로 나누어 떨어질 경우
        d[i] = min(d[i], d[i // 3] +1)

    if i % 5 == 0: # 5로 나누어 떨어질 경우
        d[i] = min(d[i], d[i // 5] +1)

print(d[x])
