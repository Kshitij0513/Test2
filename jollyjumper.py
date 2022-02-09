n=list(map(int,input().split()))
c=[]
k=0
while k!=len(n)-2:
	diff=n[k+1]-n[k+2]
	c.append(abs(diff))
	k=k+1
v=[i for i in range(1,((len(n)))-1)]	
if set(c)==set(v):
	print("Jolly")
else:
	print("Not Jolly")
 
