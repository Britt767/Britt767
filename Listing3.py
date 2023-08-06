# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 20:04:00 2023

@author: byer7
"""

lstRow = []
strFile = "MyData.txt"
objFile = None

objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")
    print(lstRow)
    print(lstRow[0] + "|" + lstRow[1] + "|" + lstRow[2].strip())
    
objFile.close()


