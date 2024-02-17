import sys
input = sys.stdin.readline
wordCount = int(input())
wordList = set()
for i in range(wordCount):
    wordList.add(input().rstrip())
print("\n".join(sorted(wordList, key=lambda x:(len(x), x))))