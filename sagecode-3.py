# (13) https://math.stackexchange.com/questions/835008/in-how-many-ways-can-7-girls-and-3-boys-sit-on-a-bench-in-such-a-way-that-every

# Answer by listing the permutations:

plst=Permutations("bbbggggggg").list()
cnt=0
for pp in plst:
    tmp = ''.join(pp)
    if tmp.count("bbb")==0 and tmp.count("g")>0 and tmp[:2] != "bb" and tmp[-2:] != "bb":
        cnt += 1
print cnt*factorial(tmp.count("b"))*factorial(tmp.count("g"))

# By recurrence:

bb,gg=3,7
def B(b,g):
    if b==0:
        return 1
    if b==1:
        return b+g
    if b==2:
        return binomial(g+2,2)
    if g==0:
        return 0
    return B(b,g-1)+B(b-1,g-1)+B(b-2,g-1)
print (B(bb,gg)-2*B(bb-2,gg-1)+B(bb-4,gg-2))*factorial(bb)*factorial(gg)

# By taylor expansion:

var('y')
taylor((1+x*y)/(1-y*(1+x+x^2)),(x,0),(y,0),10).coeff(x,3).coeff(y,7)*factorial(bb)*factorial(gg)

# By summation:

bb,gg=3,7
sum([binomial(gg-1,k)*binomial(k,bb-k-1)+binomial(gg,k)*binomial(k,bb-k) for k in [floor(bb/2)..bb]])*factorial(bb)*factorial(gg)