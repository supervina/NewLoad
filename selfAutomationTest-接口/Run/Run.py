#!/usr/bin/ python3
# -*- coding: utf-8 -*-
# @Date    : 2019-9-25
# @Author  : SunShilin
# @Version : 1.0
# @Software: Sublime


import os
print(f"initialize_path = {os.path.abspath('.')}")
PATH = os.path.abspath(".")
import sys
sys.path.append(PATH)
from Utils.ReadFile import  ReadExcel

class Run(object):

    def __init__(self,filePath):
        #Read DataFile
        test = ReadExcel()
        test.Fileread(filePath)
        print("excution completed")
if __name__ == "__main__":
	filePath = "File/interface.xlsx"
	run = Run(filePath)
