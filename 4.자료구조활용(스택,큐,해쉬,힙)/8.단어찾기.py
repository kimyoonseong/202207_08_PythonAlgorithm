import sys
from collections import deque
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
a=int(input())
p=dict()
for i in range(a):
    word=input()
    p[word]=1


for i in range(a-1):
    word=input()
    p[word]=0

for key, val in p.items():
    if val==1:
        print(key)
        break
    
    
