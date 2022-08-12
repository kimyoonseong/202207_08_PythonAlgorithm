import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,

def DFS(L,s):
    global cnt
    if L==m:
        for i in range(m):
            print(res[i],end=' ')
        print()
        cnt+=1
    else:
        for i in range(s,n+1):
            res[L]=i
            DFS(L+1,i+1)#dfs i=1일때 첫번째 가닥 i=2일때 두번째 가닥임으로 i에1더
  
if __name__=="__main__":
    n, m=map(int, input().split())
    res=[0]*(n)
    cnt=0
    DFS(0,1)
    print(cnt)
