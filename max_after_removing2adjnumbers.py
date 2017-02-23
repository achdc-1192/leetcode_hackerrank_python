# your code goes here
a = list(raw_input())
b = list()
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        b.append("".join(a[:i]+a[i+1:]))
#print b
#max = 0
#for i in range(len(b)):
#    if b[i]>max:
#        max = b[i]
#print max
print max(b)
