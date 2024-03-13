import sys

######################################

# def cal(a,b):
#   print(a+b)
#   print(a-b)
#   print(a*b)
#   print(a//b)
#   print(a%b)
#   print('%.2f'%(a/b))
  

# f1, f2 = map(int,input().split())

# cal(f1,f2)
#############################################
# def cal(a,b,c):
   
#  return(a+b+c)
  
# a,b,c = map(int,input().split())

# d =cal(a,b,c)
# e = d
# e=e/3
# print('{0}'' ''{1:0.2f}'.format(d,e)) #포메팅 {0}은 합 {1}은 평균(소수점 3자리에서 올림)
############################################
# n = int(input(),10)
# print(n<<1)
###########################################
# a,b =input().split()
# c = bool(int(a))
# d = bool(int(b))
# print(not(c)and(not d))
##############################################
# a,b = map(int,input().split())
# print(a^b)
#####################################################
# a,b,c = map(int,input().split())
# d = (a if a<b else b) if ((a if a< b else b)<c)else c
# print(d)

################################################################
# a,b,c = map(int , input().split())

# if a%2 ==0:
#   print(a)
# if b %2 ==0:
#   print(b)
# if c%2 ==0:
#   print(c)

###############################################################
# def oddeven(i):
  
#   if i<0: 
#     if i%2==0:
#      print("A")
#     else:
#      print("B")
#   else:
#     if i%2 ==0:
#      print("C")
#     else:
#       print("D")

  

# a = int(input())
# oddeven(a)
##########################################

# def result(i):
#   if i>=90:
#     print("A")
#   elif i>=70:
#     print("B")
#   elif i>=40:
#     print("C")
#   else:
#     print("D")

# a = int(input())
# result(a)


####################################

# def say(i):
#   if i=='A':
#     print("best!!!")
#   elif i == 'B':
#     print("good!!")
#   elif i == 'C':
#     print("run!")
#   elif i == 'D':
#     print("slowly~")
#   else:
#     print("what?")
  
# a = input()
# say(a)



############################################

# def month(i):
#   if i//2==0: # 1나누기 2
#    print("winter") 
#   elif i//3==1: # 3 나누기 3
#    print("spring")
#   elif i//3==2: #6 나누기 3
#     print("summer")
#   elif i//3==3: #9 나누기 3
#     print("fall")
#   elif i==12 or 2: # 12 또는 2 면 출력
#     print("winter")
    

# a = int(input())
# month(a)
##########################################

# n=1
# while n!=0: #만약 0이 같지 않다면 계속 실행
#   n = int(input())
#   if n!=0:# 만약 0이 같지 않다면 출력
#     print(n)
#   elif n==0:
#      break

###########################################
# n = int(input())


# while n!=0:
   
#     n= n-1
#     print(n) #카운트다운
##############################################
# c = ord(input())
# t = ord('a')
# while t<=c:#a부터 입력한 값까지 출력
#   print(chr(t),end=' ')
#   t+=1
#############################################

# a = int(input())

# b =0
# while b<=a:
#    print(b)
#    b= b+1 

# 또는 이방법이 있다 | |
#                 \  /
# for i in range (0, a+1):
#  print(i)

####################################################
# n=1
# letters = string.ascii_lowercase
# while n!=0:
#  a= input(''.join(choice(letters)))
#  if a == "q":
#      n=0

# while True:
#      x=input()
#      print(x)
#      if x=='q':
#           break

##############################################3
# i = int(input())
# count  =0

# for a in range(50):
#   count = count +a
#   if (count>=i):
#     print(a)
#     break
    
#########################################

# a = int(input())
# count = 0

# for i in range(50):
#   count = count + i
    
#   if (count >= a):
#         print(i)
#         break

##############################################3
# a  =input()
# a = int(a,16)
# for i in range(1, 30):
#    print('%X'%a,'*%X'%i, '=%X'%(a*i),sep='')
############################################
# a = int(input())

# for i in range(1, a+1):
 
#   if i%10==3:
#     print('X', end=' ')
#   elif i%10==6:
#     print('X', end=' ')
#   elif i%10==9:
#      print('X', end=' ')
#   else:
# #     print(i,end=' ')
  
# r,g,b = map(int,input().split())

# for i in range(0,r):
#     for j in range(0,g): 
#      for k in range(0,b):
#         print(i,j,k)
      

# print(r*g*b) #변수 바꾸니 잘됨

# a,b,c = map(int,input().split())

# for r in range(0,a):
#     for g in range(0,b): 
#      for b in range(0,c):
#         print(r,g,b)
      

# print(a*b*c) #변수 바꾸니 잘됨


# r, g, b = input().split()

# r = int(r)
# g = int(g)
# b = int(b)

# for i in range(0, r) :
#   for j in range(0, g) :
#     for k in range(0, b) :
#       print(i, j, k)

# print(r*g*b)


#########################################33
# A,B,C=map(int,input().split())
# print((A+B)%C)
# print(((A%C)+(B%C))%C)
# print((A*B)%C)
# print(((A%C)*(B%C))%C)

##########################################3

# A=int(input())
# B=input()


# print(A*int(B[2]))
# print(A*int(B[1]))
# print(A*int(B[0]))
# print(A*int(B))
####################################33


######################################
# A,B,C= map(int,input().split())

# print(A+B+C)
#############################################
# \    /\
#  )  ( ')
# (  /  )
# #  \(__)|

# print("\\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \\(__)|")
#################################################

# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|


print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")


# A,B = map(int,input().split())

# if(A<B):
#   print("<")
# elif(A>B):
#   print(">")
# elif(A==B):
#   print("==")


# def result(i):
#   if i>=90:
#     print("A")
#   elif i>=80:
#     print("B")
#   elif i>=70:
#     print("C")
#   elif i>=60:
#     print("D")
#   else:
#     print("F")

# a = int(input())
# result(a)
################################################
#윤년 2753
# a = int(input())


# if(a%4==0 and a%100!=0)or(a%400==0):
#   print(1)
# else:
#   print(0)
##########################################
# 사분면 고르기
# a = int(input())
# b=int(input())

# if(a>0 and b>0):
#   print(1)
# elif(a>0 and b<0):
#   print(4)
# elif(a<0 and b>0):
#   print(2)
# elif(a<0 and b<0):
#   print(3)
#####################################

# 알람 시계 2884
# a,b=map(int,input().split())

# if (b>=45):
#   print(a,b-45)
# elif(a>0 and b<45): #2 30 1 45  2 33 1 48
#   print(a-1,b+15)
# else:
#   print(23, b+15)



#################################################
# 오븐 시계 2525
# a,b=map(int,input().split())
# t = int(input())

# a += t//60
# b += t%60

# if b >=60:
#  a+=1
#  print(a%24,b-60)
# else:
#  print(a%24,b)
#############################################
# 오븐 시계 2525
# a,b =map(int,input().split()) # 12 45
# t=int(input())# 80
# a+=t//60# 80//60 =1 12 + 1= 13
# b+=t%60# 80%60 = 20 45 + 20 = 65
# if b >=60:
#   a+=1 # 14
#   b-=60 # 5
# elif a >=24:
#   a-=24
# print(a,b) # 14 5

# 백준 2480
# a,b,c = map(int, input().split())
# get =0  
# if (a==b and b==c) or (b==c and a==c): # 3개 다 같은 수
#   get += 10000 + a *1000
#   print(get)
# elif(((a==b or b ==c)or (c==a)) and ((b==a or a==c)or(c==b))): # 2개가 같은 수
#  if(a==b):
#    get += 1000 + a *100
#  elif(b==c):
#    get += 1000 + b *100
#  else:
#    get += 1000 + a *100
#  print(get) 
# else: # 제일 큰 수 
#   d = max(a,b,c)
#   print(d*100)
  
#2739번 백준 구구단
# a = int(input())

# for i in range(1,10):
#   c = a*i
#   print(f"{a} * {i} = {c}")


# #10950 a+b ---3
# t = int(input())
# for i in range(t) :
#   a,b =map(int,input().split())
#   print(a+b)
##########################################33
# #8393번 백준 합
# a = int(input())
# count = 0

# for i in range(50):
#   count = count + i
    
#   if (count >= a):
#         print(i)
#         break

# a = int(input())
# count=0
# for i in range(1 , a+1): # 3을 넣는다면 1 2 3 **0부터 시작하므로 반복문에 +1을 붙여야 3이 됩니다.
#   count+=i

# print(count)
#########################################3
# 영수증25304
# val = int(input())
# stuf = int(input())
# val2 =0
# for _ in range (0, stuf):
#   stuf_val,num = map(int,input().split())
 
#   val3 =stuf_val*num
#   val2 +=val3
  
# if(val==val2):
#   print("Yes")
# else:
#   print("No")
#############################################
# 25314 코딩은 체육과목입니다
# a = int(input())
# b = a//4
# for i in range(0,b):
#   if(a%4==0):
#    print("long ",end='')

# print("int")

#

################################################
# 15552 빠른 a+b
# T = int(input())
# for i in range(T):
#   a,b = map(int,sys.stdin.readline().split()) # input() 보다 처리속도가 빠르다 
#   print(a+b)

#########################################################3
#11021번 A+B ----7
# T = int(input())

# i=1
# for i in range(1,T+1):
#   a,b = map(int,input().split())
#   print(f"Case #{i}: {a} + {b} = {a+b}")

##################################3

# a = int(input())

# for i in range(1,a+1):
#     print("*"*a)

# #2439번 별찍기 ---2
# T = int(input())
# for i in range(T):
#     for j in range(4-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()

 
# a = int(input())
# for i in range(0,a+1): 
#   print("\n")     
#   for j in range(0, i+1):
#     print("*")
# #별찍기
# n = int(input())
 
# if 1 <= n <= 100:
#   for star in range(1, n+1):
#     print(" " * (n - star) + star * "*")

##############################################
# T = int(input())

# for i in range(T):
#   a,b = map(int,input().split())
#   print(a+b)
#   if (a==0 and b==0):
#     break


# T = 1
# j=0
# while(T):
#  a,b = map(int,input().split())
#  j += 1
#  print(a+b)
#  if(j==5):
#     break

# while True:
#   try:
#     a,b=map(int,input().split())
#     print(a+b)
#   except:
#     break

# N = int(input())
# list=[]
# c =0
# for i in range(N):
#    list.append(int(input()))
#    print("done")
#    b = int(input())
#    if (list == b):
#     c+=1 
      
# print(c)

# 2가지 방법
# a = int(input())
# b = map(int,input().split())
# c = int(input())
# count =0
# for i in b:
#   if i==c:
#     count+=1

# print(count)



# a = int(input())
# b = list(map(int,input().split()))
# c = int(input())

# print(b.count(c))


# a,b = map(int,input().split())
# c = list(map(int,input().split()))
# d =[0]
# for i in a:
#   if c <=b:
#     d[i] = c[i]

# print(d)
##########################################
# a = int(input())
# b = list(map(int,input().split()))

# c = min(b)
# d = max(b)
# print(c,d)
############################################
# append는 덧붙인다는 뜻으로 괄호( ) 안에 값을 입력하면 새로운 요소를 array 맨 끝에 객체로 추가한다. 요소를 추가할 때는 객체로 추가하게 되는데, 입력한 값이 리스트와 같은 반복 가능한 iterable 자료형이더라도 객체로 저장한다. 사용 예시는 아래와 같다.
#for i in range(0,9): #array.append(x) 형태로 사용한다. 



# a =[]
# for i in range(9):
#    a.append(int(input()))
  

# print(max(a))
# print(a.index(max(a))+1)

# a = input()


# print(len(a))


# T = int(input())

# for i in range(T):
#   a = str(input())
#   print(a[0]+a[-1])

# a = int(input())
# b=0
# for i in range(0,a):
#   c = 
  
#   b+=c


# print(b)

# n = input()
# b = input()
# nums=0
# for i in b:
#   nums +=int(i)

# print(nums)


# n = input()
# nums = input()
# total = 0
# for i in nums :
#     total += int(i)  # total= total+int(i)
# print(total)


# T= 1000

# for i in T:
#   a,b= map(int,input().split())
#   for j in a:
   


#          ,r'"7
# r`-_   ,'  ,/
#  \. ". L_r'
#    `~\/
#       |
#       |


# print("         ,r\'\"7")
# print("r`-_   ,'  ,/")
# print(" \. \". L_r'")
# print("   `~\/")
# print("      |")
# print("      |")


# N,M= map(int, input().split())
# basket = [0 for _ in range(N)]

# for _ in range(M):
#   i,j,k = map(int, input().split())
#   for n  in range(i,j+1):
#     basket[n-1]=k
# for n in range(N):
#   print(basket[n],end ='')




# N, M = map(int, input().split())
# basket = [0] * (N+1)

# for _ in range(M):
#     i, j, k = map(int, input().split())
#     for n in range(i, j+1):
#         basket[n] = k 

# for i in range(1, N+1):
#     print(basket[i], end = ' ')

# N=5 M=4 N은 바구니의 개수 M개의 줄  12345 바구니 i,j ==1 2 바꾼다 ==2 1 3 4 5 , 3 4 바꾼다 2 1 4 3 5 , 1 4 바꾼다 3 1 4 2 5 , 2 2 바꾼다 3 1 4 2 5 
#10813 공 바꾸기
# N,M = map(int,input().split()) # 5 4
# g= [i for i in range(1, N+1)]# g의 i열을 1~5+1까지

# for _ in range(M):# 4번 반복
#   i,j = map(int,input().split())# i,j입력
#   g[i-1],g[j-1] = g[j-1],g[i-1] #동시 지정문 다중 할당
# for k in range(N):#0~5까지 반복
#   print(g[k], end = ' ')

# #1152번 백준
# a= input().split()
# print(len(a))


# a = str(input().split())
# print(len(a.split(" ")))


#################################################3
# #2908 상수 백준
# a,b = map(int,input().split())

# a =int(str(a)[::-1])
# b =int(str(b)[::-1])
# if (a>b):
#   print(a)
# elif(a<b):
#   print(b)
################################
# a = 100
# for _ in range(a):
#   a = input()
#   print(a)
#   if (a==100):
#      break

#11718 그대로 출력하기 백준
# while True:
#   try:# 예외처리
#     print(input())
#   except EOFError:
#        break


# s = sys.stdin.readline()
# for i in s:
#   print(i.rstrip())# rstrip 이해하기
# #strip([chars]) : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거합니다.
# lstrip([chars]) : 인자로 전달된 문자를 String의 왼쪽에서 제거합니다.
# rstrip([chars]) : 인자로 전달된 문자를 String의 오른쪽에서 제거합니다


# a = str(input())
# b =str(input())
# if(b=="C4"):
#   print(a.replace('C4',''))
# if(b!='C4'):
#   print("FRULA")

# a=int(input())
# b=int(input())
# print(a*b)


# n = int(input())
# a,b =0,1
# for i in range(n):
#    a,b = b , a+b
# print(a)

# T= int(input())
# for i in range(T):
#   a,b= map(int,input().split(","))
#   print(a+b)


# a,b =map(int,input().split())
# c =list(map(int,input().split())) 
# for i in range(a):
#         if c[i]<b:
#            print(c[i],end =" ")    
    
# 상수 내림차순
# a = int(input())

# for i in range(a,0,-1):
#   print(i)
# a= list(str(input()))
# a.sort(reverse=True)
# print(int("".join(a)))
# #상수 오름차순 2750
# nums = int(input())
# num=[]
# for i in range(nums):
#   num.append(int(input()))# 리스트에 정수 값으로 nums값만큼 저장
# num.sort()# list 오름차순 정렬
# for i in range(len(num)):#num list의 리스트 갯수 만큼 반복
#   print(num[i])


# a = int(input())
# b = []
# for i in range(a):
#   b.append(int(input()))
# a.sort()
# for i in range(len(b)):
#   print(b[i])


#17478 재귀함수
# def recursive(m):
#   print("_" * (4 * (n-m)) + '"재귀함수가 뭔가요?"')

#   if not m:
#     print("_" * (4 * (n-m))+'"재귀함수는 자기 자신을 호출하는 함수라네"')
#     print("_" * (4 * (n-m))+"라고 답변하였지.")
#     return

#   print("_" * (4 * (n-m)) + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
#   print("_" * (4 * (n-m)) + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
#   print("_" * (4 * (n-m)) + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
#   recursive(m-1)
#   print("_" * (4 * (n-m)) + "라고 답변하였지.")
  

# n = int(input())
# print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# recursive(n)




#5597 과제안내신 분?

# data=[i for i in range(1,31)]

# for _ in range(28):
#   num = int(input())
#   data.remove(num)
  
  
# print(min(data))
# print(max(data))
# a =int(input())
# b=[]
# num=0

# zero =0
# for i in range(a):
  
#   b=list(input())
#   one=1
#   if(b[i] =='O'):
#     num+=one
#     one+=1
#   elif(b[i]=='X'):
#     one ==zero
#   elif(b[9]):
#     num+=3
# print(num)  

  

# a = int(input())
# b = []

# for i in range(a):
#   b.append(int(input()))
# b.sort()

# for i in range(len(b)):
#   print(b[i])



# a = int(input())
# b = []
# for i in range(a):
#   b.append(int(input()))
# a.sort()
# for i in range(len(b)):
#   print(b[i])
# nums = int(input())
# num=[]
# for i in range(nums):
#   num.append(int(input()))# 리스트에 정수 값으로 nums값만큼 저장
# num.sort()# list 오름차순 정렬
# for i in range(len(num)):#num list의 리스트 갯수 만큼 반복
#   print(num[i])


#2839 설탕배달
# a = int(input())
# bag = 0
# while a >=0:
#   if a % 5 ==0:
#     bag +=int(a//5)
#     print(bag)
#     break
#   a -=3
#   bag+=1
# else:
#  print(-1) 




# a= int(input())
# num = []
# for i in range(a):
#   num.append(int(input()))
# num.sort()
# for i in range(len(num)):
#   print(num[i])
# def solve(i ,b):
#   int g=0
#   for m in range (b):
#     g += i[n]
  


# n = int(input())
# a = []
# for i in range(n):
#   a.append(int(input()))
# solve(a,n)
# def solve(a):
#   ans = sum(a)
#   return ans


# short_men =[int(input())for _ in range(9)]
# seven_short_temp = []
# def dfs(depth,start):
#   if depth == 7:
#     if sum(seven_short_temp)==100:
#       for j in sorted(seven_short_temp):
#         print(j)
#       exit()
#     else:
#       return
#   for i in range(start, len(short_men)):
#     seven_short_temp.append(short_men[i])
#     dfs(depth+1,i+1)
#     seven_short_temp.pop()
# dfs(0,0)


# num_list = list(map(int, input().split()))
# num_list.sort()
# print(num_list[-2])


