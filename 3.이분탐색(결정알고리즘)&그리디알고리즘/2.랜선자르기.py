import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)#cnt는 len으로 나눴을때 개수
    return cnt

k,n=map(int,input().split())
Line=[]
res=0
largest=0
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest,tmp)# 둘중 비교해서 큰값 largest에 넣는함수
lt=1
rt=largest
while lt<rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
        
    else:
        rt=mid-1
print(res)
