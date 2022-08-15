import sys
sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,

n,m=map(int,input().split())
g=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b,c=map(int, input().split())
    g[a][b]=c
for i in range(1,n+1):
    for j in range( 1, n+1):
        print(g[i][j], end=" ")    
    print()
'''
for i in range(m): #가중치 없는 그래프
    a, b=map(int, input().split())
    g[a][b]=1
    g[b][a]=1
'''
