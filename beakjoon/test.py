def word_sum(s):
    sum = 0
    for c in s:
        if c == '\0' or c == ' ':
            break
        sum += ord(c) - ord('a') + 1
    return sum

def validate_input_1(s):
    return all('A' <= c <= 'Z' for c in s)

def validate_input_2(s):
    key = "TSFHHABP"
    hint = "\\BD_OBNZ"
    for i in hint:
        print(ord(i))
    for i in s:
        print(ord(i))

    print(''.join(chr(ord(s[i]) ^ ord(hint[i]) & 31) for i in range(8)))

    prv = 0
    for i in range(8):
        prv = ((prv << 1) ^ ord(s[i])) & 31
        if chr(prv + ord('A')) != key[i]:
            return False

    return True

def validate_input_3(arr):
    s1 = "computer preferred bulk tourist biographies"
    s2 = "worldwide resistance implemented magical viruses"
    s3 = "theorem"

    def sentence_sum(s):
        sum = 0
        for word in s.split():
            sum *= 100
            sum += word_sum(word) % 100
        return sum

    if arr[2] != sentence_sum(s3):
        return False

    return True

class Node:
    def __init__(self):
        self.str = ""
        self.arr = [0] * 10

def main():
    data = Node()

    data.str = input()

    if not validate_input_1(data.str):
        print("NO (1)")
        return
    print(data.arr)
    if not validate_input_3(data.arr):
        print("NO (3)")
        return

    print("YES")

if __name__ == "__main__":
    main()
