import sys
from collections import deque
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
a=input()
b=input()
p=dict()
q=dict()

for x in a:
    p[x]=p.get(x,0)+1 #(x,0): 번째 키값을 0으로 지정

for x in b:
    q[x]=q.get(x,0)+1


for i in p.keys(): #키값만 방문
    if i in q.keys():
        if p[i]!=q[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
#개선된코드
'''
a=input()
b=input()
sH=dict()
for x in a:
    sH[x]=sH.get(x, 0)+1
for x in b:
    sH[x]=sH.get(x, 0)-1

for x in a:
    if(sH.get(x)>0):
        print("NO")
        break;
else:
    print("YES")
