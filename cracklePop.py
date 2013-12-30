#!/usr/bin/env python

"""CracklyePop.py: FizzBuzz equivalent for Hacker School application."""

__author__      = "Orlando Ferrer"
__copyright__   = "Copyright 2013, Hacker School application"

###################################################################################
#A flow diagram for this program can be 
#found at: http://www.gliffy.com/go/publish/5148322
################################################################################### 

###Constant definition###
#Min and Max bounds are inclusive
c_min = 1
c_max = 100
#Define numbers to check divisibility as constants to avoid usage of magic numbers
c_3 = 3
c_5 = 5
###End constant definition###


lower = c_min #No need to adjust lower bound
upper = c_max +1 #Make upper bound inclusive
result = ""

for x in range (lower, upper):
  if x%c_3 == 0: #When divisible by 3
    result = "Crackle"
      
  if x%c_5 == 0: #When divisible by 5
    result += "Pop"
      
  if not x%c_3 == 0 and not x%c_5 == 0: #Only need to print int if not divisible
    result = x
      
  print result 
  result = ""
      
