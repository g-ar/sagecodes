# (21) https://math.stackexchange.com/questions/2094936/expected-length-of-a-sequence

am = Matrix(QQ, 6)
for i in xrange(6):
    for j in xrange(i,6):
        if i == j:
            if i == 5:
                am[i,j] = 1
                break
            am[i,j] = 2/8
        else:
            if j == 5:
                am[i,j] = 1 - sum(am[i,0:j].list())
                break
            am[i,j] = 1/8

show(am)
print sum((identity_matrix(5)-am[0:5,0:5]).inverse()[0].list())

# (22) https://math.stackexchange.com/questions/2106229/flipping-coins-and-advantages/
# Using a monte-carlo simulation
import random

ntrials = 1000000
cnt = 0
nh = 10  # total heads to win

for _ in xrange(ntrials):
    nha, nhb = 0, 0 # player a and b's number of heads obtained
    while True:
        if random.randint(0,1):
            nha += 1
        if nha == nh:
            break
        if random.randint(0,1):
            nhb += 1
        if nhb == nh:
            break
    if nha > nhb:
        cnt += 1

print cnt/float(ntrials)


# Using an absorbing Markov chain
def calc(n):
    Bm = Matrix(QQ, n^2)
    Am = Matrix(QQ, n^2)
    Cm = Matrix(QQ, n^2, 2)
    Dm = Matrix(QQ, n^2, 2)
    Zm = Matrix(QQ, n^2)

    for i in range(n):
        for j in range(n):
            Bm[n*i+j, n*i+j] = 1/2
            if j+1 != n:
                Bm[n*i+j, n*i+j+1] = 1/2
            else:
                Cm[n*i+j, 0] = 1/2

    for i in range(n):
        for j in range(n):
            Am[n*i+j,n*i+j] = 1/2
            if i+1 != n:
                Am[n*i+j, n*(i+1)+j] = 1/2
            else:
                Dm[n*i+j, 1] = 1/2

    Qm = Zm.augment(Am).stack(Bm.augment(Zm))
    Bm = Dm.stack(Cm)
    res = ((identity_matrix(n^2*2)-Qm).inverse()*Bm)[0]
    return res

print calc(10)[1]

# (23) https://puzzling.stackexchange.com/questions/57583/how-many-tries-to-roll-a-6
# expected number of 6 sided dice throws such that a 6 appears before any odd number
import numpy as np

nsum = 0
cnt = 0
ntrials = 1000000
for _ in range(ntrials):
    a = np.random.randint(1,7,100)
    if np.where((a==1)|(a==3)|(a==5))[0][0] > np.where(a == 6)[0][0]:
        cnt += 1
        nsum += np.where(a == 6)[0][0]+1

print nsum/float(cnt)
