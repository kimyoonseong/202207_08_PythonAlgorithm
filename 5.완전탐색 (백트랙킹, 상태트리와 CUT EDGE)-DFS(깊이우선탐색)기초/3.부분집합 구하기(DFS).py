import sys

#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,


def DFS(v):
    if v==n+1:
        for i in range(1,n+1):
            if ch[i]==1:
                print(i,end=' ')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)
        
if __name__=="__main__":
    n=int(input())
    ch=[0]*(n+1)
    DFS(1)
