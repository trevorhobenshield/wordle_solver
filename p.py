#arthur whitney
from functools import partial
n=2315
x=bytearray(open('../k/m','rb').read())
m=[x[i:i+n]for i in range(0,len(x),n)]

lap=lambda f,x:list(map(f,x))
ind=lambda x,y:[x[y]for y in y]

def grp(x,y,d={}):
    for x,y in zip(x,y):d[x]=d[x]+[y]if x in d else[y]
    return d

def p(x):
 a=lap(partial(ind,y=x),m)
 a=lap(lambda x:len(set(x))+(m[0][0]in x),a)
 a=a.index(max(a))
 x=[x for x in x if x!=a]
 return grp(ind(m[a],x),x).values()

g=lambda x:len(x)+(len(x)-1 if 3>len(x)else sum(lap(g,p(x))))
x=range(n)
g(x)
