import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
meeting=[]
N=int(input())
for i in range(N):
    s,e=map(int,input().split())
    meeting.append((s,e))

meeting.sort(key=lambda x : (x[1],x[0])) # 튜플 이렇게 하면 끝나는 인덱스 기준으로 정렬
et=0
cnt=0
for s,e in meeting:
    if s>=et:
        et=e
        cnt+=1

print(cnt)

