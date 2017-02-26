
s = raw_input()

d={}
#print x

for i in range(len(s)):
    if s[i] not in d:
        d[s[i]] = 1
    else:
        d[s[i]] += 1
#print d

l = list(d.values())
#print l
maxi = max(l)
mini = min(l)
maxcount = l.count(max(l))
mincount = l.count(min(l))

#print maxcount,mincount
count = 0
if maxcount > mincount or maxcount==mincount:
    for i in range(len(l)):
        if l[i]%maxi != 0:
            count += 1
else:
    for i in range(len(l)):
        if l[i]%mini != 0:
            count += 1
if count > 1:
    print "NO"
else:
    print "YES"