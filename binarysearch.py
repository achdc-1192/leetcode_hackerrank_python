def binsearch(a,value):
	low = 0
	high = len(a) - 1
	while low <= high:
		mid = (low+high)//2
		if value < a[mid]:
			high = mid - 1 
		elif value > a[mid]:
			low = mid + 1
		else:
			return mid + 1
	return None

a = [1,2,3,4,5,6,7,8]

n = len(a)
print(binsearch(a,0))
print(binsearch(a,1))
print(binsearch(a,2))
print(binsearch(a,3))
print(binsearch(a,4))
print(binsearch(a,5))
print(binsearch(a,6))
print(binsearch(a,7))
print(binsearch(a,8))
print(binsearch(a,9))