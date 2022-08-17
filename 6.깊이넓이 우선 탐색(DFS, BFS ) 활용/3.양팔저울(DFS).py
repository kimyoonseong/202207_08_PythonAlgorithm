import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
def DFS(L,sum):
    global res
    if L==n:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L+1,sum+G[L])#왼쪽
        DFS(L+1,sum-G[L])#오른쪽
        DFS(L+1,sum)#x
    
            

if __name__=="__main__":
    n=int(input())
    G=list(map(int, input().split()))
    s=sum(G)
    res=set()
    DFS(0, 0)
    print(s-len(res))
