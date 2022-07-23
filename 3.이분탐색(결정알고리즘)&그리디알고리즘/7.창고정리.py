import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,

N=int(input())
a=list(map(int,input().split()))
M=int(input())
a.sort()
for _ in range(M):
    a[0]+=1
    a[N-1]-=1
    a.sort()
    
print(a[N-1]-a[0])



