import sys

#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
def DFS(L,sum):
    global res
    if res<L:
        return
    if sum>m:
        return 
    if sum==m:
        if res>L:
            res=L
            
    else:
        for i in range(n):
            #sum+=a[i]이건왜안되는건지 모르겠다.. -> 다시 백업해서 돌아올때 sum이 15로 복귀하므로 틀림.
            DFS(L+1,sum+a[i])
        
if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    res=21470000
    a.sort(reverse=True)
    DFS(0,0)
    print(res)
