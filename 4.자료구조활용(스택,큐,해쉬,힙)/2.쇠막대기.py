import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
s=input()
stack=[]
cnt=0

for i in range(len(s)):
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
