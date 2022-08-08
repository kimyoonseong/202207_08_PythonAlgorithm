import sys

#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
def DFS(L,sum,tsum):
    global result
    if sum+(total-tsum)<result:         #total-tsum은 아직 부분집합에 포함되지않은것
        return
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum#이렇게하면 로컬(지역)변수
    else:
        DFS(L+1, sum+a[L],tsum+a[L])
        DFS(L+1,sum,tsum+a[L])
if __name__=="__main__":
    c,n=map(int,input().split())
    a=[0]*n
    result=-21470000
    for i in range(n):
        a[i]=int(input())
    total=sum(a)
    DFS(0,0,0)
    print(result)
