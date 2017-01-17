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
