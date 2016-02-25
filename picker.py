#!/usr/bin/env python
# picker.py


# Title:        Random Person Picker for the Office
# Author:       Rebecca Bilbro
# Date:         2/24/16
# Organization: Commerce Data Service, U.S. Department of Commerce


"""
If we need to draw names out of a hat.  Allows you to choose the number of people you want to select
"""

#####################################################################
# Imports
#####################################################################
import random

people = {1  :  "Sasan Bahadaran",
          2  :  "Pamela Bell",
          3  :  "Radhika Bhatt",
          4  :  "Rebecca Bilbro",
          5  :  "Mark Brown II",
          6  :  "Jeffrey Chen",
          7  :  "Tyrone Grandison",
          8  :  "Negar Kalbasi",
          9  :  "Ian Kalin",
          10 :  "Natassja Linzau",
          11 :  "Priyanka Oberoi",
          12 :  "Burton Reist",
          13 :  "Alison Rowland",
          14 :  "Tonja White",
          15 :  "Star Ying"}



#prompt user for number of sample
numOfPeople = input("Please enter the number of people you want to select:")

dictCount = range(1,len(people)+1)
diceThrow = random.sample(dictCount,numOfPeople)
iter = 0
for number in diceThrow:
	iter+=1
	print "pick #%s: %s" %(iter,people[number])
