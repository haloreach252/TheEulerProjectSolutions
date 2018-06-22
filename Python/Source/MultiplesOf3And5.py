s=0
n=0
for n in range(1,1000):
	if n%5==0 or n%3==0:
		s = s + n
		n + 1
		print(str(s))