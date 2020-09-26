def solution(board, moves):
    answer, b_len, output = 0, len(board), []

    for i in moves:
        for j in range(b_len):    # topdown
            if board[j][i-1] != 0:
                if not len(output):  # 비어있을때 채우고
                    output.append(board[j][i-1])
                    board[j][i-1] = 0
                    break
                if output[-1] == board[j][i-1]:  # 이전이랑 같을때 이전꺼 없애고
                    answer += 2
                    output.pop()
                    board[j][i-1] = 0
                    break
                output.append(board[j][i-1])
                board[j][i-1] = 0
                break

    return answer*2


'''
다른풀이, 간결하지만 append와 pop횟수 늘어서 연산 증가

for i in moves:
    for j in range(len(board)):
        if board[j][i-1] != 0:
            stacklist.append(board[j][i-1])
            board[j][i-1] = 0

            if len(stacklist) > 1:
                # 2개 비교해서 pop 2번
                if stacklist[-1] == stacklist[-2]:
                    stacklist.pop(-1)
                    stacklist.pop(-1)
                    answer += 2     
            break
'''
