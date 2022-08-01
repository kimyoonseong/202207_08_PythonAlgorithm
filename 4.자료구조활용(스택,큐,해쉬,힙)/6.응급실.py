import sys
from collections import deque
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
n,m=map(int,input().split())
Q=[(pos,val) for pos, val in enumerate(list(map(int,input().split())))]
Q=deque(Q)
cnt=0
while True:
    cur=Q.popleft()
    #cur[1]은 튜플의 두번째것을 가르킴
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            break
print(cnt)
