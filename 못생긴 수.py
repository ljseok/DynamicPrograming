n = int(input())

ug = [0] * n # 못생긴 수를 담기위한 테이블 초기화
ug[0] = 1

id2 = id3 = id5 = 0 # 인덱스 초기화
mul2, mul3, mul5 = 2, 3, 5 # 곱셈 초기화

for i in range(1,n):
   ug[i] = min(mul2,mul3,mul5) # 가능한 곱셈 중에서 최소값 찾기

   if ug[i] == mul2: # 곱셈이 2라면
       id2 += 1
       mul2 = ug[id2] * 2 # 2를 곱한다

   if ug[i] == mul3: # 곱셈이 3이라면
       id3+= 1
       mul3 = ug[id3] * 3 # 3을 곱한다

   if ug[i] == mul5: # 곱셈이 5라면
       id5 += 1
       mul5 = ug[id5] * 5 # 5를 곱한다.

print(ug[n-1]) # 못생긴 수 출력