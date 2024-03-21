file = open("resources/problem11.txt", "r")
s = file.read()
numbers = []
num=""
def conv(s, current):
    current = ''
    for char in s:
        if char != ' ':
            current.join(char)
            print(char)
            print(current)
        else:
            numbers.append(current)
            s = s[1:]
            conv(s, '')

conv(s, '')
print
