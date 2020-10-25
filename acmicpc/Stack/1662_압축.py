'''
Error Handling
- 메모리초과, 스택에 '괄호' push가 많을 때
- 파싱 오류, 반례 : 6(22)122
'''
# 숫자만 들어있는 배열 만들기 ['33', '562', '71', '9']
N = list(map(str, input().split("(")))

print(N)
'''
메모리 초과
ex) 9(9(9(9(9(9(9(9(9(9(9(9(9(9(9(9(9(9(9(9(9(9(9(9(111)))))))))))))))))))))))) 

answer = N[-1]
for i in range(len(N)-2, -1, -1):
    kq = int(N[i][-1]) * answer
    answer = N[i][0:-1] + kq
'''

# 길이를 구해서, 압축해제에 길이만 다루기
answer = len(N[-1])
for i in range(len(N)-2, -1, -1):
    kq = int(N[i][-1]) * answer
    answer = len(N[i][0:-1]) + kq

print(answer)
