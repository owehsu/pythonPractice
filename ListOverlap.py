def listOverlap():
	a = [1,1,2,3,5,8,13,21,34,55,89]
	b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	c = []
	for i in range(len(a)):
		index = a[i]
		for i in range(len(b)):
			if b[i] == index:
				if b[i] not in c:
					c.append(b[i])
	print(c)
