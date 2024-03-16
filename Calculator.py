def cal(a,b):
  print(a+b)
  print(a-b)
  print(a*b)
  print(a//b)
  print(a%b)
  print('%.2f'%(a/b))
f1, f2 = map(int,input().split())

cal(f1,f2)