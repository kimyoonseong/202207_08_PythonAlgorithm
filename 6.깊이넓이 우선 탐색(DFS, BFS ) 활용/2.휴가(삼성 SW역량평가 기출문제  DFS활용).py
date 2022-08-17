import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
def DFS(L,sum):
    global res
    
    if L==n+1:
        if sum>res:
            res=sum
    else:
        if L+pv[L]<=n+1:
            DFS(L+pv[L],sum+pt[L])
        DFS(L+1,sum)#상담안할때
            

if __name__=="__main__":
    n=int(input())
    pv=list()
    pt=list()
    for i in range(n):
        a, b=map(int, input().split())
        pv.append(a)
        pt.append(b)
    res=-21470000
    pv.insert(0,0)
    pt.insert(0,0)
    DFS(1,0)
    print(res)
