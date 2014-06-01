# (1)
# https://math.stackexchange.com/questions/798412/expected-value-of-a-sum-of-a-10-sided-die
# g.f. by  Marko Riedel
# code explains better 
var('p q')
nn=10    # Number of die faces
ns=101   # Total is at least ns
fx=taylor((1-x)/(1-x-x*(1-x^(nn))/nn),x,0,ns)
summ=0
for q in range(1,nn+1):
    summ += sum(x^(nn-p+1),p,1,nn-q+1)*x^(ns-q)/nn*fx.coefficient(x,ns-q)
print diff(summ,x).subs(x=1)


# (2)
# https://math.stackexchange.com/questions/811516/probability-that-yz-1-xz-2/   

var('i')
fxt=taylor((30+sum((1/x^i-1/x^(i*31))/(1-1/x^i),i,1,9))*(20+sum((x^i-x^(i*21))/(1-x^i),i,1,9))/(200*300),x,0,200)
print sum([fxt.coefficient(x,i) for i in range(1,181)])


# (3)
# 'n' numbers are chosen randomly and uniformly in (0,1). What is the probability that the sum of their 
# cubes is less than 1 ?   
# In general, we use the convolution of probability densities when considering the sums.
# So, for any power, we can write as:

k=5/7  # sum of x_i^(7/5) 's
f(z)=diff(z^k,z)
f2(z)=f(z)
for i in range(10):
    f2(z)=integrate(f2(z-y)*f(y),y,0,z)
    fbet=integrate(f2(z),z,0,1)
    print i+2, N(fbet)
    
# Following that, we can proceed to find a general formula
# Since it's a product of Beta functions, the simplified formula we get is:

f(n,k)=1/n*k^(n-1)*gamma(k)^n/gamma(n*k)
N(f(4,1/4))  # Probability of (sum x_i^4) < 1   i=1..4