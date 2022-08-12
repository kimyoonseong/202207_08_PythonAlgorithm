import sys

#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,

def DFS(L,sum):
    
    if L==n and sum==f:
        for x in p :
            print(x,end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
             if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1,sum+(p[L]*b[L])) #sum에 p배열 b배열(이항계수) 곱해줘야한다.
                ch[i]=0
  
if __name__=="__main__":
    n, f=map(int, input().split())
    p=[0]*n
    b=[1]*n
    ch=[0]*(n+1)
    for i in range(1, n):#1~3까지 b 배열에다
        b[i]=b[i-1]*(n-i)//i
    DFS(0,0)
