#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 21:50:59 2018

@author: alemeneses
"""



from exercises2 import checkout


#%%


list1 = (["guitar", "pick_box", "guitar_strings"])
list2 = (["guitar", "pick_box", "guitar_strings, pick_box"])
list3 = [([""])

def test_checkout (): 
    assert checkout(list1)== 1015
    assert checkout(list2)== 1020
    assert checkout(list3)== False
   
    
    


