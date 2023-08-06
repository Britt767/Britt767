# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 20:04:00 2023

@author: byer7
"""

lstRow = []
strFile = "MyData.txt"
objFile = None

objFile = open(strFile, "w")
lstRow = ["1", "Brian Smith", "BSmith@hotmail.com"]
objFile.write(lstRow[0] + ',' + lstRow[1] + ',' + lstRow[2] + '\n')

objFile.close()
