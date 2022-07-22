import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
meeting=[]
N=int(input())
for i in range(N):
    s,e=map(int,input().split())
    meeting.append((s,e))

meeting.sort()
meeting.reverse()
print(meeting)
cnt=0
largest=0

for s,e in meeting:
    if e>largest:
        largest=e
        cnt+=1
print(cnt)
