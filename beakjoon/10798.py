import sys

words = sys.stdin.readlines()
for i in range(15):
    for j in range(5):
        try:
            if words[j][i] != "\n":
                print(words[j][i], end="")
        except:
            pass
