def solution(cards1, cards2, goal):
    while True:
        if len(cards1)!=0 and cards1[0]==goal[0]:
            cards1.remove(cards1[0])
            goal.remove(goal[0])
        elif len(cards2)!=0 and cards2[0]==goal[0]:
            cards2.remove(cards2[0])
            goal.remove(goal[0])
        else:
            return "No"
        if len(goal)==0:
            return "Yes"

print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))