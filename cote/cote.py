l = int(input())

for i in range(l):
    l = list(input())
    if l[-1] == "(":
        print("NO")
    else:
        s = []
        for j in l:
            if (s == []) or (j == s[-1]):
                s.append(j)
            elif s[-1]+j == "()":
                s.pop()
        if len(s)==0:
            print("YES")
        else:
            print("NO")