def mergesort(a):
	if len(a) > 1:
		mid = len(a)//2
		a1 = a[:mid]
		b1 = a[mid:]

		mergesort(a1)
		mergesort(b1)

		i,j,k = 0,0,0
		while i < len(a1) and j < len(b1):
			if a1[i] < b1[j]:
				a[k] = a1[i]
				i += 1
			else:
				a[k] = b1[j]
				j += 1
			k += 1
		while i < len(a1):
			a[k] = a1[i]
			i += 1
			k += 1
		while j < len(b1):
			a[k] = b1[j]
			j += 1
			k += 1
	print("merge sort result is ", a)

	return a



a = [3,1,1,5,7,6,2,4,4,6,9,8]

print(mergesort(a))