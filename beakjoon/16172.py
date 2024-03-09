import sys
input = sys.stdin.readline

text=input()
k=input()

def extract_letters(text):
    return ''.join(char for char in text if not char.isdigit())

result = extract_letters(text)
if k in result:
    print(1)
else:
    print(0)