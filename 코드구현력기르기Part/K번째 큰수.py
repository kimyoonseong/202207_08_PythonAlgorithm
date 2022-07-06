import sys
sys.stdin=open("A.txt","rt")

N,K=map(int,input().split())
a=list(map(int,input().split()))
res=set()#set은 중복을 제거해준다.sort 함수안됨


for i in range(N):
    for j in range(i+1,N):
        for m in range(j+1,N):
            res.add(a[i]+a[j]+a[m])

res=list(res)
res.sort()
res.reverse()
print(res[K-1])



