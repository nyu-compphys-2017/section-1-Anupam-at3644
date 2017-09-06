from __future__ import division
import numpy as np
""" 
    Func->f
    No_Rect->n
    lower_bound->l
    upper_bound->u    
"""
def Riemann (f,n,l,u):
    width=(u-l/n)
    x_vals=np.arange(l+width,u+width,width)
    fn_values=f(x_vals)
    result=np.sum(width*fn_values)
    return result

def square(x):
    return x**2

print(Riemann(square,10,0,1))


    

