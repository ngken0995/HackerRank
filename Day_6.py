t = int(input())
for i in range(0, t):
    s = input()
    a = []
    b = []
    for j in range(0,len(s)):
        if j == 0:
            a.append(s[j])
        elif j%2 == 1:
            b.append(s[j])
        elif j%2 == 0:
            a.append(s[j])
    a =''.join(a)
    b =''.join(b)
    print(f'{a} {b}')
