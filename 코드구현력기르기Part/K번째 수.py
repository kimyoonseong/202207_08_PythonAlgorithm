import sys
#sys.stdin=open("A.txt","rt")
T=int(input())
for t in range(T):
    n,s,e,k=map(int, input().split())#n:개 s:시작지점 e : 끝지점 k:번째
    a=list(map(int, input().split()))
    a=a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1,a[k-1]))
 
