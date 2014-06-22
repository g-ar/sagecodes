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

# (14) https://math.stackexchange.com/questions/838659/football-game-penalty-kicks-maximizing-winning-chances

cnt=0  
cnt3=0
cnt4=0
cnt5=0               # these count variables are not necessary, just there for a check
p=4/5
q=1-p
def prob(a,b,nn):
    global cnt,cnt3,cnt4,cnt5
    if nn == 6:
        if abs(a-b)==3:
            cnt3+=1
            return nn*p^(a+b)*q^(nn-a-b)
    if nn == 8:
        if abs(a-b)>=2:
            cnt4+=1
            return nn*p^(a+b)*q^(nn-a-b)   
    if nn==10:
        if a==b: 
            cnt=cnt+1
            return (nn+25/4)*p^(a+b)*q^(nn-a-b)    # 25/4 : exp.# kicks after a draw
        else:
            cnt5+=1
            return nn*p^(a+b)*q^(nn-a-b)           
    return prob(a+1,b,nn+2)+prob(a,b+1,nn+2)+prob(a+1,b+1,nn+2)+prob(a,b,nn+2)
tmp=prob(0,0,0)                  # gets the expected no. of kicks required to end game
print tmp,N(tmp),cnt,cnt3,cnt4,cnt5

# (15) https://math.stackexchange.com/questions/656310/8-cards-are-drawn-from-a-deck-of-cards-without-replacement

n=[4]*10+[16]
nn=8
sum(sum(a*sum(sum([binomial(n[a],i)*binomial(n[a-1]*(a-1),nn-i-j)*binomial(52-n[a]-(a-1)*n[a-1],j) for i in [nn-k-j+1..n[a]]]) for j in [nn-k-n[a]+1..nn-k]) for a in [1..10]) for k in [6..8])/binomial(52,8)

