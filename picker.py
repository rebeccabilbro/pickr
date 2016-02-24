#!/usr/bin/env python
# picker.py


# Title:        Random Person Picker for the Office
# Author:       Rebecca Bilbro
# Date:         2/24/16
# Organization: Commerce Data Service, U.S. Department of Commerce


"""
If we need to draw names out of a hat.
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

diceThrow = random.randrange(1,16)
print(people[diceThrow])
