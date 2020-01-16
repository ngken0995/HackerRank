t = int(input())
word = []
for i in range(0, t):
    s = input()
    word.append(s)
    
for j in range(0,len(word)):
  a=[]
  b=[]
  for k in range(0,len(word[j])):
    if k == 0:
      a.append(word[j][k])
    elif k%2 == 1:
      b.append(word[j][k])
    elif k%2 == 0:
      a.append(word[j][k])
  a =''.join(a)
  b =''.join(b)
  print(f'{a} {b}')

#Using function

def wordgroup():
  global word
  t = int(input())
  for i in range(0, t):
    s = input()
    word.append(s)
  return word

def separate(word):
  for j in range(0,len(word)):
    a=[]
    b=[]
    for k in range(0,len(word[j])):
      if k == 0:
        a.append(word[j][k])
      elif k%2 == 1:
        b.append(word[j][k])
      elif k%2 == 0:
        a.append(word[j][k])
    a =''.join(a)
    b =''.join(b)
    print(f'{a} {b}')
    
word=[]    
wordgroup()
separate(word)
