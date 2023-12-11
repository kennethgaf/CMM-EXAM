import numpy as np

def gsection(ftn, xl, xm, xr, tol = 1e-9):
    # applies the golden-section algorithm to maximise ftn
    # we assume that ftn is a function of a single variable
    # and that x.l < x.m < x.r and ftn(x.l), ftn(x.r) <= ftn(x.m)
    
    # In this context, xm is an initial guess x-value for the optimum point
    #
    # The algorithm iteratively refines x.l, x.r, and x.m and
    # terminates when x.r - x.l <= tol
    
    # To convert to a minimization code, you need to switch
    # the sign of the inequality tests in the if statements on lines 24 and 38.
    
    
    gr1 = 1 + (1 + np.sqrt(5))/2
    #
    # successively refine x.l, x.r, and x.m
    fl = ftn(xl)
    fr = ftn(xr)
    fm = ftn(xm)
    while ((xr - xl) > tol):
        if ((xr - xm) > (xm - xl)):
            y = xm + (xr - xm)/gr1
            fy = ftn(y)
            if (fy >= fm):
                xl = xm
                fl = fm
                xm = y
                fm = fy
            else:
                xr = y
                fr = fy
        else:
            y = xm - (xm - xl)/gr1
            fy = ftn(y)
            if (fy >= fm):
                xr = xm
                fr = fm
                xm = y
                fm = fy
            else:
                xl = y
                fl = fy     
    return(xm, ftn(xm))
    
xl=0
xm=2
xr=10
def ftn(x):
    return 2*np.sin(x)-(x**2/10)
print(gsection(ftn, xl, xm, xr, tol = 1e-9))
