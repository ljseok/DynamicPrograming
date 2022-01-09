n = int(input()) # 식량창고의 개수 입력받기
arr = list(map(int,input().split())) # 데이터 입력받기

d = [0] * 100 # 리스트를 초기화

d[0] = arr[0] # 배열의 첫번째 원소를 넣고
d[1] = max(arr[0], arr[1]) # 두개중 큰 값을 비교해서 넣는다.

for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + arr[i]) # i-1 번째의 값과 i-2번째의 값 에다가 현재 식량창고를 더한값을 비교해서 더 큰값을 고른다.

print(d[n-1])
