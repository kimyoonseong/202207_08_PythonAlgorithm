import sys
import itertools as it
sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,

n, f=map(int, input().split())
b=[1]*n
cnt=0
for i in range(1, n):
    b[i]=b[i-1]*(n-i)/i
a=list(range(1, n+1))

for tmp in it.permutations(a):
    sum=0
    for L, x in enumerate(tmp):
        sum+=(x*b[L])
    if sum==f:
        for x in tmp:
            print(x, end=' ')
        break
