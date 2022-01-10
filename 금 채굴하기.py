for test in range(int(input())): # 테스트 케이스 정보 입력
    n,m = map(int,input().split()) # 금광의 정보를 입력 (행과 열에 대한 정보 )
    arr = list(map(int, input().split()))

    Dynamic = []
    inx = 0
    for i in range(n):
        Dynamic.append(arr[inx:inx+m])
        inx += m

    for j in range(1,m): # 열에대한 정보를 확인
        for i in range(n): # 행에대한 정보를 확은
            if i == 0: # 블록의 위치를 벗어난 경우
                left_up = 0
            else: # 벗어나지 않았다면
                left_up = Dynamic[i-1][j-1]
            if i == n-1: # 블록의 위치를 벗어난 경우
                left_down = 0
            else: # 벗어나지 않았다면
                left_down = Dynamic[i-1][j-1]
            left = Dynamic[i][j-1] # 왼쪽에서 오는 경우
            Dynamic[i][j] = Dynamic[i][j] + max(Dynamic[i-1][j-1],Dynamic[i][j-1], Dynamic[i-1][j-1]) # 왼쪽 위 , 왼쪽 , 왼쪽 아래

    result = 0
    for i in range(n):
        result = max(result,Dynamic[i][m-1]) # 오른쪽 열에 있는 값에서 최대의 값 출력
    print(result)




