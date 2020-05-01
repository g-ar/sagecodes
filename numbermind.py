from z3 import *
import sys

def main():
    sol = Solver()
    fname = "input.txt"
    is_sol_distinct = True
    
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        
    if len(sys.argv) > 2:
        is_sol_distinct = sys.argv[2] == "1"

    numbers = []
    hints = []
    
    with open(fname, "r") as fo:
        lines = fo.readlines()

        for l in lines:
            n, h = l.split(";")
            numbers.append([int(i) for i in n.split(',')])
            hints.append([int(i) for i in h.split(',')])
            
    cols = len(numbers[0])
    a = numbers
    
    # variables
    x = [Int("x[%d]" % j) for j in range(cols)]
    
    # constraints
    '''
    All are distinct
    '''
    if is_sol_distinct:
        sol.add(Distinct(x))
  
    '''
    All numbers 0 <= x_i <= 9
    '''
    for i in range(cols): 
        sol.add(x[i] >= 0, x[i] <= 9)

    for i in range(len(a)):
        sol.add(Sum([If(x[c] == a[i][c],1,0) for c in range(cols)]) == hints[i][1])
    
    cnt = 0
    while sol.check() == sat:
        mod = sol.model()
        xval = [mod.eval(x[j]).as_long() for j in range(cols)]
        cond = True

        for i in range(len(a)):
            cond &= (len(set(xval) & set(a[i])) == hints[i][0])
            
        if cond:
            cnt += 1
            print(xval)
        sol.add(Or([x[i] != mod.eval(x[i]).as_long() for i in range(cols)])) # add constraint to check for different solution
          
    print("#solutions: ", cnt)

if __name__ == "__main__":
    main()
