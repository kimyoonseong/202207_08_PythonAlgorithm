import sys
from collections import deque
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
ch=[[0]*n for _ in range(n)]
sum=0
Q=deque()
ch[n//2][n//2]=1#중앙지
sum+=a[n//2][n//2]
Q.append((n//2, n//2))
L=0
while True:
    if L==n//2:
        break
    size=len(Q)
    for i in range(size):
        tmp= Q.popleft()
        for j in range(4):
            x=tmp[0]+dx[j]#시계방
            y=tmp[1]+dy[j]
            if ch[x][y]==0:
                sum+=a[x][y]
                ch[x][y]=1
                Q.append((x,y))
    L+=1
print(sum)
