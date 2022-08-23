import sys
#from collections import deque
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
def DFS(x, y):
    global cnt
    cnt+=1
    board[x][y]=0
    for i in range(4):
        if 0<=x+dx[i]<n and 0<=y+dy[i]<n and board[x+dx[i]][y+dy[i]]==1:
            DFS(x+dx[i],y+dy[i])
        
if __name__=="__main__":
    n=int(input())
    board=[list(map(int, input())) for _ in range(n)]
    res=[]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                cnt=0
                DFS(i, j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)
