n=input()
for _ in xrange(n):
    s=list(raw_input())
    l=len(s)
    count=0
    for i in xrange(1,l):
        dic={}
        for j in xrange(l-i+1):
            t=str(sorted(s[j:j+i]))
            k=dic.setdefault(t,0)
            #print k,t+" k and t \n"
            dic[t]+=1
            #print dic[t], " dict output\n"
        for j in dic:
            #print j,dic[j],"elements in dcit \n"
            count+=((dic[j])*(dic[j]-1))/2
            #print count,"count output"
    print count