x = [[4,'a'], [2,'b'], [1, 'x']]
y = [[4,'a'], [2,'b'], [1, 'x']]
print x + y
x.sort()
print x
for i in x: i[0] +=1
print x

d = {'a':'aa', 'b':'bb'}
for i in d: print i, d[i]

s="01234567"
print s[2:-1],'\n============'

import time
print int(time.time())
print dir(time.time)