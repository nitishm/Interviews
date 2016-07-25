def removeDupLetter():
    s = "cbacdcbc"
    d = [0] * 26
    op = ""
    for c in s:
        index = ord(c) - ord('a')
        if not d[index]:
            d[index] = 1
        else:
            continue
    index = 0
    for i in d:
        if i:
            op += chr(index + ord('a'))
        index = index + 1 
    return op

print removeDupLetter()
print ord('a')