import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
def DFS(v):
    global cnt
    if v==n:
        cnt+=1
        #for x in path:
        #    print(x, end=' ')
        #print()
    else:
        for i in range(1, n+1):
            if g[v][i]==1 and ch[i]==0:
                ch[i]=1
                #path.append(i)
                DFS(i)
                #path.pop()
                #print("s")
                ch[i]=0



if __name__=="__main__":
    n, m=map(int, input().split())
    g=[[0]*(n+1) for _ in range(n+1)]
    ch=[0]*(n+1)
    for i in range(m):
        a, b=map(int, input().split())
        g[a][b]=1
    cnt=0
    ch[1]=1
    #path=list()
    #path.append(1)
    DFS(1)
    print(cnt)
