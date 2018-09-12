# your code goes here
a = list(input())
b = list()
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        b.append("".join(a[:i]+a[i+1:]))
print b
maxi = 0
for i in range(len(b)):
    if b[i]>maxi:
        maxi = b[i]
print maxi