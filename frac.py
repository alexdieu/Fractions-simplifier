## VERY poor code by alexdieu
n = input("Grade:")
v = input("%s on :" % n)
g = input("Put %s/%s on how much (15/25 = 12/20 so i answer 20 if i want that)?\n"% (n,v))
n = float(n)
v = float(v)
g = float(g)
r = (n/v)*g
print("result %s/%s" % (r,g))
