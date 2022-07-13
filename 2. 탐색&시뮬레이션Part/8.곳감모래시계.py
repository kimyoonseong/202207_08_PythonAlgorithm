import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,






n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
m=int(input())
#회전
for i in range(m):
    h, t, k=map(int,input().split()) #h:행 t:방향 k:횟수
    if t==0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0)) #맨앞에거 pop하고 맨뒤에 append
    else:
        for _ in range(k):
            a[h-1].insert(0,a[h-1].pop())#맨뒤에 pop하고 그걸 맨앞에 insert
                      
#합
res=0
s=0
e=n-1
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)
