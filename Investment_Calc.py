# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:33:23 2024

@author: LTeinfalt
Last updated: 09/15/2024

"""
def investment_calc(r, n, C0):
    #Calculates future value of an investment

    FV = C0*(1+r)**n
    
    print("Future value of an $" + '{0:4.2f}'.format(C0) + " investment at " + '{0:1.3f}'.format(r) 
          + " annual interest rate after " + '{0:3.0f}'.format(n) + " years will be =  " 
          + '${0:5.2f}'.format(FV))          

    return FV


def main():

    """7% annual interest rate is expressed as 0.07
    Compounded over 10 years
    Initial investment of $1000
    """
    
    """ r = interest rate
        n = number of compounding periods
        C0 = cash available at time t=0
        FV = the future value of the investment
    """
    r = 0.07
    n = 10
    C0 = 1000
    FV = investment_calc(r, n, C0)

if __name__ == '__main__':
    main()

