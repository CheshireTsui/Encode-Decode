x = [[4,'a'], [2,'b'], [1, 'x']]
y = [[4,'a'], [2,'b'], [1, 'x']]
print x + y
x.sort()
print x
for i in x: i[0] +=1
print x
l = ['a', 'b', 'c','d','e']
print "".join(l)
print l[0:3]
print 2.743/100,'\n============'

d = {'a':'aa', 'b':'bb'}
print d.keys()
for i in d: print i, d[i]
print 'a' in d, 'aa' in d,'\n============'

s="01234567"
print s[2:-1],'\n============'

print range(3),'\n============'

import time
print int(time.time())
print dir(time.time)