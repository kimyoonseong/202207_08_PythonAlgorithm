import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
s=input()
stack=[]
cnt=0
result=0
res=''
for i in s:
    if i.isdecimal(): # i가 10진수일때
        stack.append(int(i))

    else:
        
        if i=='*':
            R=int(stack.pop())
            L=int(stack.pop())
            stack.append(R*L)
            
        elif i=='/':
            R=int(stack.pop())
            L=int(stack.pop())
            stack.append(R/L)
        
            
        elif i=='+':
            R=int(stack.pop())
            L=int(stack.pop())
            stack.append(R+L)
           
        
        elif i=='-':
            R=int(stack.pop())
            L=int(stack.pop())
            stack.append(L-R)
            
for i in stack:
    print(i)
        
    







'''
    else:
        if i=='(':
            stack.append(i)
        elif i=='*'or i=='/':
            while stack and (stack[-1]=='*'or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(i)
        elif i=='+'or i=='-':
            while stack and stack[-1]!= '(':
                res+=stack.pop()
            stack.append(i)
        elif i==')':
            while stack and stack[-1]!= '(':
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)

'''
