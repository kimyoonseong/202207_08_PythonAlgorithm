import sys

#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,

def DFS(x):
    if x==0 :
        return;
    else:
        DFS(x//2)
        print(x%2,end="")

if __name__=="__main__":
    n=int(input())
    DFS(n)

