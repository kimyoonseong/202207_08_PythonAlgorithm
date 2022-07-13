import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,



#내가푼방법 100점



#강의 코드
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
res=0
s=e=n//2#s 앞 e 뒤

for i in range(n):
    for j in range(s,e+1):#처음엔 2,2
        res+=a[i][j]
    if i<n//2:#가운데 전까진 s는 - e는 +해준다
        s-=1
        e+=1
    else:     #가운데 이후론 s는 + e는 - 해준다
        s+=1
        e-=1
print(res)

