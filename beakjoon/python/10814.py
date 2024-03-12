import sys

wordList = sys.stdin.readlines()[1:]
wordList.sort(key=lambda x: int(x.split()[0]))
print("".join(wordList))