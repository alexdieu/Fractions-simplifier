## VERY poor code by alexdieu
n = input("Note:")
v = input("%s sur :" % n)
g = input("Mettre %s/%s sur combien (15/25 = 12/20 donc je reponds 20 si je veux ca)?\n"% (n,v))
n = float(n)
v = float(v)
g = float(g)
r = (n/v)*g
print("ca fait %s/%s" % (r,g))
