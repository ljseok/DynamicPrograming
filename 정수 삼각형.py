n = int(input())
DyanmicPro = [] # 테이블 초기화

for _ in range(n):
    DyanmicPro.append(list(map(int, input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j == 0: # 인덱스 범위를 벗어난 경우
            left_down = 0
        else:
            left_down = DyanmicPro[i-1][j-1] # 왼쪽 위에서 내려온 경우

        if j == i: # 인덱스 범위를 벗어난 경우
            down_straight = 0
        else:
            down_straight = DyanmicPro[i-1][j] # 위에서 바로 내려온 경우

        DyanmicPro[i][j] = DyanmicPro[i][j] + max(left_down, down_straight) # 원래있던 테이블에 최대값을 더한다
print(max(DyanmicPro[n-1])) # 최댓값 출력

