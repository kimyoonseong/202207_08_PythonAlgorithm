import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
def Count(capacity):
    cnt=1
    sum=0
    for x in Music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
  
    return cnt





    
n,m=map(int,input().split()) 
Music=list(map(int,input().split()))  
lt=1
rt=sum(Music)
maxx=max(Music)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)
