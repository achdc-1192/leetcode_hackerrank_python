a = [5,3,4,6,1]
sum = 9
d = {}
#l = []
for i in (a):
    res = sum - i
    if res not in d:
        d[i]=False
    else:
        print i,res#l.append((i,res))
print d