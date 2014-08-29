# (18) http://math.stackexchange.com/questions/854039/biology-how-to-find-the-probability-of-randomly-generating-multiple-sequential

st="ATGCAGC"                              # The string pattern 
rep=2                                     # no of times the pattern is to be repeated   
nn=len(st)                                # The string length
mx=[[0]*(nn+1) for i in range(nn+1)]     # The initialized directed graph
nchars=4                                  # Number of possible characters
for i in range(1,nn):                    
    seen=st[:i]                           # The substring seen till index 'i'
    seenst=set(seen)                      # Unique chars seen
    
# Get the proper transition state, by watching the repeated substrings
# E.g. in 123121, 
#  consider the states to be "others", "1", "12", "123", "1231", "12312" and "123121"
#  If we see 123123, we must go to the state "123" from "12312"
    for ele in seenst:                   
        nlongest=0                       
        tmpst=seen+ele                       
        for k in range(1,len(tmpst)):
            if st.find(tmpst[-k:]) == 0:  # The last k chars in the state
                nlongest=k
        mx[i][i+1]=1
        if st[i] != ele and nlongest != 0:
            mx[i][nlongest]=1
    mx[i][0]=nchars-sum(mx[i])
mx[0][0]=(nchars-1) 
mx[0][1]=(1)
am=matrix(mx[:nn][:])
am=am.augment(zero_matrix(QQ,nn,rep*nn-1))
bm=matrix(QQ,0,am.ncols())
for i in range(rep+1):
    for j in range(nn):
        tmp=(am[j,:]).list()
        bm=bm.stack(matrix((tmp[-i*nn:])+(tmp[:-i*nn])))
bm[bm.nrows()-rep:bm.nrows(),0]=0
nn=7000
print N(sum(((bm^(nn))[0,bm.ncols()-len(st):bm.ncols()]).list())/4^nn)

# and a simulation in python -- slow, but worth a check

import random
trials=10000
cnt1,cnt2,cnt3=0,0,0
for i in range(trials):
    rlst=''.join(map(str, random.sample(range(1,5)*7000,7000)))
    if ''.join(rlst).count('1234134')==1:        
        cnt1+=1
    if ''.join(rlst).count('1234134')==2:        
        cnt2+=1
    if ''.join(rlst).count('1234134')==3:        
        cnt3+=1
print cnt1/float(trials),cnt2/float(trials),cnt3/float(trials)

# (19) https://math.stackexchange.com/questions/911571/probability-rolling-a-dice-5-times/

var('y z')
ff = expand((2*x+3*y+z)^5)
summ = 0
for i in range(0,5):
    for j in range(i+1,6):
        summ += ff.coeff(x,j).coeff(z,i).subs(y=1)
print summ/6^5