import sys

#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,


def DFS(L,sum):#L은 인덱스번호,
    if sum>total//2:
        return
    if L==n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0)            
    else:
        DFS(L+1,sum+a[L])#사용 0
        DFS(L+1,sum)#사용 x
        
if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    total=sum(a)
    DFS(0,0)
    print("NO")
