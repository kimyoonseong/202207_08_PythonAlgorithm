import sys
from collections import deque
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,

queue=[]
cnt=0
n,m=map(int,input().split())
for i in range(1,n+1):
    queue.append(i)
queue=deque(queue)

#강의코
'''
while queue:
    for _ in range(m-1):
        cur=queue.popleft()
        queue.append(cur)
    queue.popleft()
    if len(queue)==1:
        print(queue[0])
        queue.popleft()
'''

#40점.... 이유는 모르겠음 (고침 cnt가 3번마다 왕자한명씩 제거.
while queue:
    
    if cnt%m==m-1:
        queue.popleft()
        #print(cnt)
        cnt+=1
        #print(queue)
        
    else:
        cur=queue.popleft()
        queue.append(cur)
        cnt+=1
    if len(queue)==1:
        print(queue[0])
        queue.popleft()


