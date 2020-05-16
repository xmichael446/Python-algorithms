# Euklid

def Euklid(a, b):
	if a == b:
		return a
	else:
		if a > b:
			return Euklid(b, a-b)
		else:
			return Euklid(a, b-a)
			
print(Euklid(128, 32))