def solution(board, moves):
    new_board=list(map(list,zip(*board))) # 2차원배열을 뒤집음
    blanket=[]
    global count
    count=0
    for x in range(len(new_board)):
        if 0 in new_board[x]:
            del new_board[x][0:new_board[x].count(0)]  # 0떼고 숫자만 남김
    print(new_board)
    for y in moves:
        try:
            blanket.append(new_board[y-1][0])
            
            del new_board[y-1][0]
            if len(blanket)>1:
                if blanket[-1]==blanket[-2]:  #새로들어온게 그전꺼랑 같으면 삭제한다.
                    count+=2
                    del blanket[-1]
                    del blanket[-1]
        except:
            continue
        


    return count
        

 
 
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))