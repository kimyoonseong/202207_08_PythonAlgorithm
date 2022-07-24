import sys

#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
N=int(input())
a=list(map(int,input().split()))
cnt=0
lt=0
rt=N-1
last=0
res=""
tmp=[]
while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt],'L'))
    if a[rt]>last:  
        tmp.append((a[rt],'R'))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        res=res+tmp[0][1]#LR을 가르킴
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()

print(len(res))
print(res)
