"""def solution(numbers, hand):
    result=''
    leftnow=-3
    rightnow=-3
    for x in numbers:
        if x==1 or x==4 or x==7:
            result=result+'L'
            leftnow=x
        elif x==3 or x==6 or x==9:
            result=result+'R'
            rightnow=x
        else:
            if abs(leftnow+2-x)<abs(rightnow-x):
                leftnow=x
                result=result+'L'
            elif abs(leftnow+2-x)==abs(rightnow-x):
                    if hand=='right':
                        rightnow=x
                        result=result+'R'
                    else:
                        leftnow=x
                        result=result+'L'
            else:
                rightnow=x
                result=result+'R'

    return result
""" # 25점 한손이 2,5,8,0 에 있을때 제대로 작동안함 abs(leftnow+2-x)알고리즘 수정해야함
def solution(numbers, hand):
    answer = ''
    
    # 키패드 좌표료 변경
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    # 시작 위치
    left_s = dic['*']
    right_s = dic['#']
    
    for i in numbers:
        now = dic[i]
        # 1, 4, 7을 누르는 경우 무조건 왼손
        if i in [1, 4, 7]:
            answer += 'L'
            left_s = now
            
        # 3, 6, 9를 누르는 경우 무조건 오른손
        elif i in [3, 6, 9]:
            answer += 'R'
            right_s = now
            
        # 2, 5, 8, 0을 누르는 경우
        else:
            left_d = 0
            right_d = 0
            
            # 좌표 거리 계산해주기
            for a, b, c in zip(left_s, right_s, now):
                left_d += abs(a-c)
                right_d += abs(b-c)
            
            # 왼손이 더 가까운 경우
            if left_d < right_d:
                answer += 'L'
                left_s = now
                
            # 오른손이 더 가까운 경우
            elif left_d > right_d:
                answer += 'R'
                right_s = now
            
            # 두 거리가 같은 경우
            else:
                # 왼손잡이 경우
                if hand == 'left':
                    answer += 'L'
                    left_s = now
                    
                # 오른손잡이 경우
                else:
                    answer += 'R'
                    right_s = now
            
    return answer



 
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))