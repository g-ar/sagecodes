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

# (16) https://math.stackexchange.com/questions/846442/generating-function-probability-regaridng-coin-toss/

var('h t')
fht=1/(1-(t+h*(t+h*(t+h*(t+h*(t+h*t))))))*(1+h*(1+h*(1+h*(1+h*(1+h)))))
fhtt=taylor(fht,(h,0),(t,0),25)
fhtt.coeff(t,8).coeff(h,17)/2^25

# (17) http://math.stackexchange.com/questions/850857/an-archery-game/851331#851331

def prob_consecutive(probA=1/2, probB=1/2, numA=2, numB=3, winner=0):
    '''
    probA and probB are player 0's and player 1's hitting probabilities
    numA and numB are the number of times they need to consecutively hit the target to win
    If winner=0, it calculates the probability for player 0 to win, similarly for winner=1.
    '''
    pa = probA
    pb = probB
    qa = 1-pa
    qb = 1-pb
    eqns = []
    varstr = ''
    nA = numA
    nB = numB
    nn = max(nA,nB)
    ql = [[0]*(nn+2) for i in [0..nn+2]]
    d1 = {}
    q  =  var(','.join('q%s%s'%(i,j) for i in range(nA+1) for j in range(nB+1)));
    for i in range(0,nA+1):
        for j in range(0,nB+1):
            if i<nA and j>=nB:
                ql[i][j] = winner
            if i>=nA and j<nB:          
                ql[i][j] = 1-winner
            if i<nA and j<nB:
                ql[i][j] = q[(nB+1)*i+j]
    for i in range(0,nA+1):
        for j in range(0,nB+1):
            if i<nA and j<nB:
                eqns.append(q[(nB+1)*i+j] == pa*qb*ql[i+1][0]+qa*pb*ql[0][j+1]+pa*pb*ql[i+1][j+1]+qa*qb*ql[0][0]) 
                d1[str(q[(nB+1)*i+j])] = q[(nB+1)*i+j]           
    varstr = ','.join('q%s%s'%(i,j) for i in range((nB+1)) for j in range((nB+1)) if i<nA and j<nB) 
    sols = sage_eval('solve('+str(eqns)+','+varstr+')',locals = d1);
    return (sols[0][0]).rhs()
prob_consecutive(3/4,43/50,10,12)

# Slightly modified equation for the winner when the constraint of consecutive hits is removed.

def prob_nonconsecutive(probA=1/2, probB=1/2, numA=2, numB=3, winner=0):
    '''
    probA and probB are player 0's and player 1's hitting probabilities
    numA and numB are the number of times they need to hit the target to win
    If winner=0, it calculates the probability for player 0 to win, similarly for winner=1.
    '''
    pa = probA
    pb = probB
    qa = 1-pa
    qb = 1-pb
    eqns = []
    varstr = ''
    nA = numA
    nB = numB
    nn = max(nA,nB)
    ql = [[0]*(nn+2) for i in [0..nn+2]]
    d1 = {}
    q  =  var(','.join('q%s%s'%(i,j) for i in range(nA+1) for j in range(nB+1)));
    for i in range(0,nA+1):
        for j in range(0,nB+1):
            if i<nA and j>=nB:
                ql[i][j] = winner
            if i>=nA and j<nB:          
                ql[i][j] = 1-winner
            if i<nA and j<nB:
                ql[i][j] = q[(nB+1)*i+j]
    for i in range(0,nA+1):
        for j in range(0,nB+1):
            if i<nA and j<nB:
                eqns.append(q[(nB+1)*i+j] == pa*qb*ql[i+1][j]+qa*pb*ql[i][j+1]+pa*pb*ql[i+1][j+1]+qa*qb*ql[i][j]) 
                d1[str(q[(nB+1)*i+j])] = q[(nB+1)*i+j]           
    varstr = ','.join('q%s%s'%(i,j) for i in range((nB+1)) for j in range((nB+1)) if i<nA and j<nB) 
    sols = sage_eval('solve('+str(eqns)+','+varstr+')',locals = d1);
    return (sols[0][0]).rhs()
prob_nonconsecutive(3/4,43/50,10,12,1)    