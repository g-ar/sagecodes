# (8)
# What's the expected value of c in the following snippet of code?
#
# c = 0
# a = 0
# while (a!=0xffffffff)     # loop until all 32 bits in 'a' are 1
#     i = random(0,32)      # get a random integer between 0 and 31
#     a = a|(1<<i)          # set the i'th bit from right in a 32 bit integer 'a'
#     c = c+1               # increment c

#    (i) Using an absorbing markov chain
n = 32
mx = [[0]*(n+1) for i in range(n+1)]
mx[0][1] = 1
for i in range(1, n):
    mx[i][i] = i/n
    mx[i][i+1] = 1-i/n
mx[n][n] = 1
am = matrix(mx)
print sum((identity_matrix(n)-am[0:n, 0:n]).inverse()[0].list())

#    (ii) For any 'n' -- it's just a coupon collector's problem in disguise
def h(n): return sum([1/i for i in range(1, n+1)])   # n'th harmonic number
print 32*h(32)

# (9)
# What's the expected value of c in the following snippet of code?
#
# c = 0
# a = 0
# while (a!=0xffffffff)     # loop until all 32 bits in 'a' are 1
#     i = random(0,32)      # get a random number between 0 and 31
#     a = a^(1<<i)          # toggle the i'th bit from right in a 32 bit integer 'a'
#     c = c+1               # increment c

#    (i) Using an absorbing markov chain

n = 32
mx = [[0]*(n+1) for i in range(n+1)]
mx[0][1] = 1
for i in range(1, n):
    mx[i][i-1] = i/n
    mx[i][i+1] = 1-i/n
mx[n][n] = 1
am = matrix(mx)
print sum((identity_matrix(n)-am[0:n, 0:n]).inverse()[0].list())

#    (ii) For any 'n', using the following algorithm obtained by solving a recurrence for expectation

ax = 1
n = 32
summ = 0
i = 0
while i < n:
    ax = (ax*i+x)/(x-i)
    summ += ax
    i += 1
print summ.subs(x=n)

# (10) https://math.stackexchange.com/questions/827568/how-many-ways-can-n-spaces-be-used-with-blocks-of-size-le-n-or-leave-empty
# Getting the sequence to examine it:

for nn in range(16):
    cnt = 0
    for i in range(nn+1):
        plst = Partitions(i).list()
        for p in plst:
            cnt += Permutations(p+[0]*(nn-i)).cardinality()
    print cnt,

# (11) https://math.stackexchange.com/questions/823422/what-is-the-number-of-condensed-products-in-each-term-of-this-sequence
# Counting it by counting!

var('k');
q = var(', '.join('q%s'%i for i in range(20)));
nn = 16
a = [0]*20
a[0] = q0
for i in range(nn):
    a[i+1] = expand(q[i+1]*sum([a[k]*a[i-k] for k in [0..i]]))
    print str(a[i]).count('+')+1,
print str(a[nn]).count('+')+1

# (12) https://math.stackexchange.com/questions/835458/expected-value-of-two-successive-heads-or-tails-stuck-on-computation
# An absorbing markov chain

var('p q')
q = 1-p
am = matrix([
    [0, p, q, 0, 0],
    [0, 0, q, p, 0],
    [0, p, 0, 0, q],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
])
ami = (identity_matrix(3)-am[:3, :3]).inverse()[0, :]
f(p) = sum(ami.list()).full_simplify()
