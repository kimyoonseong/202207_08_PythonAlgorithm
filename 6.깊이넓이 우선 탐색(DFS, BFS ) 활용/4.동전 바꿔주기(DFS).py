import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
def DFS(L,sum):
    global cnt
    if sum>n:
        return
    if L==m:
        if sum==n:
            cnt+=1

    else:
         for i in range(cn[L]+1):
            DFS(L+1, sum+(cv[L]*i))
    
            

if __name__=="__main__":
    n=int(input())
    m=int(input())
    cv=list()
    cn=list()
    for i in range(m):
        a,b=map(int,input().split())
        cv.append(a)
        cn.append(b)
    cnt=0
    DFS(0, 0)
    print(cnt)
