import sys

#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
def DFS(L):
    global cnt
    if L==m:
        for i in range(m):
            print(res[i],end='')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            res[L]=i
            DFS(L+1)
    
if __name__=="__main__":
    n,m=map(int,input().split())
    res=[0]*m
    cnt=0
    DFS(0)
    print(cnt)
