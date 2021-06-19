n = int(input())
s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))
flag = 0
for i in range(1,n+1):
    if i in s1[1:] or i in s2[1:]:
        flag = 1
    else:
        print("Oh, my keyboard!")
        flag = 0
        break
if flag == 1:
    print("I become the guy.")
