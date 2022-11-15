# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:38:30 2022

@author: nelso

lecture: nov(11) 7 2022 after 2 hours about
"""
#import loan


from os import chdir
chdir('D:/cs177/madeinclass')

import loanclass  #loanclass

#pg 192 in text
class finance(loan):
    def __init__ (self, name):
        super().__init__(name)
        #super()._ratePct
    
    
    def value401k(self, pmt, months, intapr, currentd):
        # how much money will i have after 
        # 'months' given a current value 
        # of 'currentd' by putting 'pmt' in to the 
        # 401k account, assuming interset 
        # intAPR
        
        value = (currentd + pmt*((1+intapr/1200)**months -1) / (intapr/1200))
        return value
    

    def futval(self, pmt, intr, nmonths):
        _r = intr/1200 #convert apr into decimal/months
        _F = (pmt*(1-_r)**nmonths - 1) / _r
        return _F
    
    def payout_annuity(self, valueannuity, intr, nmonths):
        
        # intR is annual rate, yield to maturity
        _r = intr/1200
        _pmtpermo = ((valueannuity * _r * (1+_r)**nmonths)/ ((1+_r)**nmonths) -1)
        #_pv_annuity = (valueannuity/_r)*(1-(1+_r)**(-nmonths))
        return(_pmtpermo)#return(_pv_annuity)



if __name__ == "__main__":
    finMgt = finance('myfinance')
    
    value = finMgt.Value401k(50 , 60, 2.0 , 10000)
    print(f"value of 401k = {value: .2f}")
    
    nmonths = 36 * 12
    intrate = [3.5, 5.5, 8.5]
    for r in intrate:
        fval = finMgt.futval(500, r, nmonths)
        print(f"r = {r: 0.2f}, Annuity value = {fval: .2f}")

    
    finMgt.setPmt(20)
    finMgt.setRate(2)
    finMgt.setPV(100)
    finMgt.setMonths(60)
    
    v = finMgt.computePmt(finMgt._Pmt, finMgt._months, finMgt._ratePct, 200)
    #print(v)
    print(f"value of savings : {v: .2f}")
    
    
    valann = 786333.07
    nmonths = 15*12
    pmtpermo= finMgt.payout_annuity(valann, 5.5, nmonths)
    print(f"present value of the annuity: {pmtpermo: .2f}")
    






