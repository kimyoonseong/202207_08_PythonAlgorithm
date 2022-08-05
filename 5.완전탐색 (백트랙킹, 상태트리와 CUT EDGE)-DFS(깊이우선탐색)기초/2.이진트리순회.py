import sys

#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,


def DFS(v):
    if v>7:
        return
    else:  
        print(v, end=' ')
        DFS(v*2)
        DFS(v*2+1)
        
if __name__=="__main__":
    DFS(1)
