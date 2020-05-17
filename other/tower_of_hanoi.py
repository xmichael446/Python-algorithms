def hanoi(n , source, dest, aux): 
	if n==1: 
		print("Disk 1 from peg",source,"to peg",dest)
		return "Done"
	hanoi(n-1, source, aux, dest) 
	print("Disk",n,"from peg",source,"to peg",dest) 
	hanoi(n-1, aux, dest, source)

print(hanoi(4, 1, 3, 2))