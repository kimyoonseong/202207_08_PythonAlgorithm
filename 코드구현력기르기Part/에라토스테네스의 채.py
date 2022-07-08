import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))

N=int(input())
cnt=0
ch=[0]*(N+1)
for i in range(2,N+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i,N+1,i):
            if ch[j]==0:
                ch[j]=1
print(cnt)
