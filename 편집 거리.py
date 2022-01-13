def edit_dist(st1, st2):
    n = len(st1)
    m = len(st2)

    Dynamic = [[0] * (m+1) for _ in range(n+1)] # 2차원 테이블 초기화

    for i in range(1,n+1):
        Dynamic[i][0] = i
    for j in range(1,m+1):
        Dynamic[0][j] = j

    for i in range(1,n+1): # 최소 편집거리를 계산
        for j in range(1,m+1):
            if st1[i-1] == st2[j-1]: # 두 문자가 같은경우
                Dynamic[i][j] = Dynamic[i-1][j-1] # 왼쪽위에 해당하는 수를 그대로 대입
            else: # 두 문자가 다른경우
                Dynamic[i][j] = 1 + min(Dynamic[i][j-1],Dynamic[i-1][j],Dynamic[i-1][j-1])
                # 왼쪽으로 부터 삽입, 위쪽으로 부터 삭제 , 왼쪽위로부터 교채
    return Dynamic[n][m]

st1 = input() # 첫번째 문자열 입력
st2 = input() # 두번째 문자열 입력

print(edit_dist(st1, st2))