import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,

def DFS(L,s,sum):
    global cnt
    if L==m:
        if sum%f==0:
            cnt+=1
        
    else:
        for i in range(s,n):
            DFS(L+1,i+1,sum+a[i])#dfs i=1일때 첫번째 가닥 i=2일때 두번째 가닥임으로 i에1더
  
if __name__=="__main__":
    n, m=map(int, input().split())
    a=list(map(int,input().split()))
    f=int(input())
    cnt=0
    DFS(0,0,0)
    print(cnt)
