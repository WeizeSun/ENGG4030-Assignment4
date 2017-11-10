sf = open('shakespeare_single', 'r').read().split('\n')[:-1]
gf = open('gutenberg_single', 'r').read().split('\n')[:-1]
af = open('gutenberg_A_single', 'r').read().split('\n')[:-1]
bf = open('gutenberg_B_single', 'r').read().split('\n')[:-1]
cf = open('gutenberg_C_single', 'r').read().split('\n')[:-1]

s = set([x.split()[0] for x in sf])
g = set([x.split()[0] for x in gf])
a = set([x.split()[0] for x in af])
b = set([x.split()[0] for x in bf])
c = set([x.split()[0] for x in cf])

sug = s.union(g)
sua = s.union(a)
sub = s.union(b)
suc = s.union(c)
sig = s.intersection(g)
sia = s.intersection(a)
sib = s.intersection(b)
sic = s.intersection(c)

print "sug: {0}".format(len(sug))
print "sua: {0}".format(len(sua))
print "sub: {0}".format(len(sub))
print "suc: {0}".format(len(suc))
print "sig: {0}".format(len(sig))
print "sia: {0}".format(len(sia))
print "sib: {0}".format(len(sib))
print "sic: {0}".format(len(sic))
