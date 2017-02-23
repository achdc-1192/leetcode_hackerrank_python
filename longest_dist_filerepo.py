import sys
import os
l = []
while True:
    a = sys.stdin.readline()
    if a:
        l.append(a)
    else:
        break
for i in range(len(l)):
    l[i] = l[i].strip("\n")
print l

s = 0
spaces = 0
spaces_array []
for i in reversed(range(len(l))):
    line = l[i]
    #print line
    if line.find(".gif") != -1 or line.find(".jpeg") != -1:
        spaces_array.append(s)
        s=0
        spaces = len(line) - len(line.strip())
        #print spaces, line
    if (spaces > (len(line) - len(line.strip()))):
        s += len(line.strip()) + 1
        #print s
        spaces -= 1

return max(spaces_array)
