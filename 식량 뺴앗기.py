'''
n = int(input())  # 정수 입력 받기
array = list(map(int, input().split())) # 식량 정보 입력받기
'''

n = 4
array=[1,3,1,5]

d = [0] * 100 # 테이블 초기화

# 동적 프로그래밍

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1]) # 결과값 출력