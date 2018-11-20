#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 01:15:21 2018

@author: alemeneses
"""

#%%

from exercises2 import checkout_insurance_priority
 
list1 = (["guitar", "insurance", "priority_mail", "insurance", "priority_mail"])
list2 =(["guitar"])
list3 = ([""])
list4 = (["guitar", "priority_mail", "insurance"])

def test_checkout_insurance_priority ():
    assert checkout_insurance_priority (list1)== False
    assert checkout_insurance_priority (list2)== 1000
    assert checkout_insurance_priority (list3)== False
    assert checkout_insurance_priority (list4)== 1015
  