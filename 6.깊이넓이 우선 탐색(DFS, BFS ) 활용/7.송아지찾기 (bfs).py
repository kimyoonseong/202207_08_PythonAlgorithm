import sys
from collections import deque
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
MAX = 10000
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
n,m = map(int,input().split())
ch[n] = 1#시작
dis[n] = 0#거리는 0
dQ = deque()
dQ.append(n)
while dQ:
    now=dQ.popleft()
    if now==m:
        break
    for next in(now-1, now+1, now+5):
        if 0<next<=MAX:
            if ch[next]==0:#방문 안했을때만
                dQ.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[now])
