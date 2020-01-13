num = int(input())
phonebook={}
for i in range(0,num):
    c = input().split()
    phonebook[c[0]] = c[1]

while True:
    try: 
        c = input()
    except EOFError:
        break

    if c in phonebook:
        print(f'{c}={phonebook[c]}')
    else:
        print('Not found')
