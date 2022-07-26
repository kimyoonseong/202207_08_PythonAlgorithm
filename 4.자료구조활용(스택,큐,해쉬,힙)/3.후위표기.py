import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
s=input()
stack=[]
cnt=0
res=''
for i in s:
    if i.isdecimal(): # i가 10진수일때
        res+=i
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
            
    if s[i]== '+' or '-' or '/' or '*':
        stack.append(s[i])
    elif (s[i]=='*'or '/') and s[i-1]=='*'or '/':
        stack.pop(s[i-1])
        res.append(s[i-1])
        stack.append(s[i])
    if s[i]=='('
        stack.append(s[i])
        
    
    if s[i]=='(':
        stack.append(s[i])
    else:
        if s[i-1]=='(':
            stack.pop()
            cnt+=len(stack)
        elif s[i-1]==')':
            stack.pop()
            cnt+=1
print(cnt)
'''
