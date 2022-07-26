import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
num,m=map(int, input().split())

num=list(map(int, str(num)))#하나하나 접근할수있다
stack=[]
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
#print(stack)
#res=''.join(map(str,stack))
#print(res)
for x in stack:
    print(x,end='')
