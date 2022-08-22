import sys
#from collections import deque
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
def DFS(x,y):
    global cnt
    if x==6 and y==6:
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy]==0:
                board[xx][yy]=1
                DFS(xx,yy)
                board[xx][yy]=0


if __name__== "__main__":
    board=[list(map(int,input().split())) for _ in range(7)]
    cnt=0
    board[0][0]=1
    DFS(0,0)
    print(cnt)
