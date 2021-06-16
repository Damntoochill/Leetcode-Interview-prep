string = '{]'
dict = {'{':'}','[':']','(':')'}
stack = []
for char in string:
    if char in ['{','(','[']:
        stack.append(char)
    else:
        if stack:
            top = stack.pop()
            if dict[top] != char:
                print("NO")
                break
        else:
            print('NO')
            break
if stack:
    print("No")
else:
    print("YEs")
