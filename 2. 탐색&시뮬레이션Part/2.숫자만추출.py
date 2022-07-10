import sys
sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))


s=input()
res=0
for i in s:
    if i.isdecimal():
        res=res*10+int(i)
        
    
print(res)
cnt=0
for i in range(1,res+1):
    if res%i==0:
        cnt+=1
print(cnt)
