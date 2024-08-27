# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 23:21:57 2024

@author: SHIVANGI
"""

## inputs we need from the user
#total rent
#total food ordered for snacking
#electricity units spend
#charge per unit
#persons living in room

##output
#total amount you've to pay is 

rent = int(input("enter you hostel rent ="))
food = int(input("enter the amount of food ordered ="))
electricity_spend = int(input("enter the total of electricity spend ="))
charge_per_unit = int(input("enter the charge per unit ="))
persons = int(input("enter the number of persons living in room = "))


total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("each person will pay = ", output)