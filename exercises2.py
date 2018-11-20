#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 20:56:18 2018

@author: alemeneses
"""

#%%

# Our e-shop sells the following products:

#   1. Guitar: $1000
#   2. Pick box: $5
#   3. Guitar Strings: $10

#   Create a function named checkout that takes a list that represents a 
#   shopping cart and returns the total cost of it.  This function should  
#   check that the shopping cart must not be empty.

#   Create also some tests for the function.  Try to think of the corner cases.

#   Hint: you can represent a product as a dictionary with a name and a price.

prices =[1000, 5, 10]

def checkout ():
    
    guitars = int(input(" How many guitars do you want? "))
    pick_box = int(input("How many pick box do you want? "))
    guitar_strings =int(input("how many guitar strings do you want? "))
    
    
    items = [guitars, pick_box, guitar_strings]
    
    shopping_cart = []
    
    for i in range (0, len(prices)):
       shopping_cart.append(prices[i]*items[i])
       
       total_cost = sum (shopping_cart)
    
    if total_cost == 0 :
        print ("there are no items in your shopping cart")
    else: 
        return (total_cost)
    
#%%
# problem 1 solved with a dictionary: 

prices2 = {"guitar" : 1000, "pick_box" : 5, "guitar_string" : 10}


def checkout2 (shopping_cart2): 
    cost2=0
    if shopping_cart2 == []:
        return "not possible" 
    
    else: 
        for i in shopping_cart2:
            cost2 += int(prices2[i])
        
    return "Total bill" + str(cost2) 
    
    
    
    #%%
#  You want to give more features to the user, so you decide that you will 
#  allow them to purchase an insurance package on their purchase and also priority 
#  mail.  Consider that these two new services can only be purchase 
#  once per order.

#   1. Insurance: $5
#   2. Priority mail: $10

#   Modify your checkout function so it handles these cases correctly, and 
#   add more tests that check your functionality.
    
prices3 = {"guitar" : 1000, "pick_box" : 5, "guitar_string" : 10,
           "insurance": 5, "priority_mail" : 10}

def checkout3 (shopping_cart3): 
   cost3=0
   if shopping_cart3 == []:
        return "not possible" 
    
   else: 
       for i in shopping_cart3:
            cost3 += int(prices3[i])
          
            
   count_insurance = shopping_cart3.count("insurance")

   count_priority_mail = shopping_cart3.count("priority_mail")     
            
   if count_insurance > 1 :
        return (" You can only buy 1 insurance")
        
            
   elif count_priority_mail > 1:
        return (" You can only order 1 priority mail")
        
            
   else:
        return "your total cost is " + str(cost3)

    
    
    
    
    
    
    