with open('vocabulary.txt') as f:
    tem=[]
    for x in f:
        tem=x.strip().split(':')
        t=input("{}:".format(tem[1]))
        if t==tem[0]:
            print("맞았습니다.")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(tem[0]))