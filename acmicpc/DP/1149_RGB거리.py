N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]

for i in range(N):
    for j in range(3):
        if i == 0:  # 0행은 그대로 삽입
            dp[i][j] = array[i][j]
        else:
            '''
            # Debug
            print('target', dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])
            print('array', array[i][j])
            '''

            '''
            1열 선택시, 전 행의 2, 3열중 min 선택
            => 자기자신의 행을 제외하고 나머지 행의 최솟값을 현재값에 누적
            '''
            dp[i][j] = min(dp[i-1][(j+1) % 3], dp[i-1]
                           [(j+2) % 3]) + array[i][j]

print(min(dp[-1]))
