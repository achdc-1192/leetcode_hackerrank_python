a = "viking"
s= ""
i = 0
count = len(a)
while i < len(a):
	if len(a)-1-i == 0:
		s += a[:count]
	elif a[len(a)-1-i] == " ":
		s += a[len(a)-1-i+1:count] + " "
		count= len(a)-1-i
	i += 1

print(s)
if len(a) == len(s):
	print("correct")
else:
	print("false")