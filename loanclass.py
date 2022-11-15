# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 19:21:38 2022

@author: nelso
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:43:35 2022

@author: 16617
"""
import numpy as np

class loan(object): #loanpy
    def __init__ (self, name):  # initialize with a name, thie permits
                                # easier manamgement of multiple instances
        """
        loanpy is a class object to implement computations of 
        loan parameters
        
        name documents data set

        Returns
        -------
        None.

        """
        #initialization
        self._name = name
        self._Pv = 0
        self._intAPR = 0
        self._Pmt = 0
        self._nMonths=0
        
        
    def getName(self):
        print(f"\nname on this instance: {self._name}")
    
    def getChoice(self):
        print("\nwhat would you like to compute?")
        print("options: Pmt, Pv, intAPR, nMonths")
        
        choice = 0
        
        while choice  not in ("Pmt", "Pv", "intAPR", "nMonths"):
            choice = input("enter choice ")
            
        if choice == "Pmt":
            self.getPmt()
        elif choice == 'Pv':
            self.getPv()
        elif choice == 'rateAPR':
            self.getIntRate()
        else:
            self.get_nMonths()


    def getIntRate(self):#replace with functions listed in assignment#
        ''' Solve for interest rate, APR  '''
        self._Pv = float(input('Enter PV '))
        self._Pmt = float(input('Enter Pmt '))
        self._nMonths = int(input('Enter number of months '))
        
        # The solution will be r where using Pmt, n, and Pv works
        ## bisection algorithm finds the two sides of the equation are equal
        ## that is, the difference is 0
        ## side 1: Pmt*(1-(1+r)**(-n))
        ## side 2:  Pv*r
        
        #example of an in-line (lambda) function
        fIntRate = lambda r: self._Pmt*(1-(1+r)**(-self._nMonths)) - self._Pv*r
        
        # low and high possible interest rates, APR
        # the actual rate is between 
        
        _rlow =0
        _rhigh = 50 
        
        _rl = _rlow/1200
        _rh = _rhigh/1200
        _count = 0
        
        while(_count < 20): # in case there is no solution
            _rTry = (_rl+_rh)/2
            if abs(fIntRate(_rTry)) < 0.001: break
            
            if fIntRate(_rTry) > 0: _rl = _rTry
            else: _rh = _rTry
            
            _count += 1
            
        if(_count >=20):
            print("no solution: try again")
            print(f"interest rate APR is > {_rTry*1200:.2f}%") # convert back to APR
            rTry = None
        
        print(f"interest rate ={_rTry}")
        return _rTry*1200

    def getPmt(self):#replace with functions listed in assignment##
        self._Pv = float(input('Enter PV '))
        self._intAPR = float(input('Enter APR '))
        self._nMonths = int(input('Enter number of months '))
        #assumes you entered interest rates as APR
        
        _r = self._intAPR/1200
        self._Pmt = _r *self._Pv/(1-(1+_r)**-self._nMonths)

        print(f'{self._Pmt}')
        print('left for you to do')
        pass
    
    def get_nMonths(self):
        self._Pv = float(input('Enter PV '))
        self._Pmt = float(input('Enter Pmt '))
        self._intAPR = float(input('Enter APR '))
        #self._nMonths = -np.log(1-self._PV*_r/self._Pmt)/np.log(1+_r)
        #self._nMonths = -np.log(1-self._PV/(_r*self._PV))/np.log((1+_r))
        
        _r = self._intAPR/1200
      
        self._nMonths = -np.log(1-self._Pv*_r/self._Pmt)/np.log(1+_r)

        print(f'{self._nMonths}')
        #print('left for you to do')
        pass
    
    def getPv(self):
        self._Pmt = float(input('Enter Pmt '))
        self._intAPR = float(input('Enter APR '))
        self._nMonths = int(input('Enter number of months '))
        
        _r = self._intAPR/1200
        self._Pv = (self._Pmt / _r) * (1 - (1 + _r)**(-self._nMonths))
        
        print(f'{self._Pv}')
        pass
####################################################################
"""THIS ONE IS NOT FINISHED"""
#####################################################################     
  
if __name__ == '__main__':
    
    testloan = loanpy('example1')
    testloan.getName()
    
    testloan.getChoice()