#!/usr/bin/env python3

# Author: Christian Bargraser

# INSTANCE ATTRIBUTES
# ###################
# 
# self.strKey: str
#     - Key for encoding/decoding vigenere cypher (whitespace is removed)
# 
# self.iKeyLen: int
#     - Length of self.strKey
#
# self.strXM: List[str]
#     - Column headers for Vigenere Square (referenced by self.strKey)
#
# self.strYM: List[str]
#     - Row headers for Vigenere Square (referenced by encoded/decoded text)
#
# self.strGridM: List[List[str]]
#     - Vigenere Square (does not include column and row headers)
#     - Validated with __isValidGrid
#
# self.iLen: int
#     - Length of self.strXM, which is the same length as self.strYM
#
# self.bKeepUnknown: bool
#     - Keep characters that are not in self.strAlphaM
#
# FUNCTIONS
# #########
# 
# def __init__(self, strKey: str, strXM: List[str]=lman.listAlpha(), strYM: List[str]=lman.listAlpha(), strGridM: np.ndarray=lman.listToNpGrid(lman.listAlpha()), bKeepUnknown: bool=True):
#     - strXM default: ['A', 'B', ... 'Y', 'Z']
#     - strYM default: ['A', 'B', ... 'Y', 'Z']
#     - strGridM default:
#           [['A', 'B', ... 'Y', 'Z']
#            ['B', 'C', ... 'Z', 'A']
#            ['C', 'D', ... 'A', 'B']
#            ...
#            ['Z', 'A', ... 'X', 'Y']]
# 
# def __isValidGrid(self) -> bool:
#     - Return True if self.strGridM is a valid Vigerene Square, False otherwise
#     - Ensures all rows have the same elements
#     - Ensures that all rows are the same length
# 
# IMPLEMENTED FUNCTIONS
# #####################
# 
# def encodeStr(self, strLine: str, iShift: int, strOutputFile: str=None) -> str: 
# def decodeStr(self, strLine: str, iShift: int, strOutputFile: str=None) -> str:
# 
# INHERITED FUNCTIONS
# ###################
# 
# def encodeFile(self, strInputFile: str, iShift: int, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
# def decodeFile(self, strInputFile: str, iShift: int, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
# def coderFile(self, bEncode: bool, strInputFile: str, iShift: int, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:

import re
from .. import lman
from .. import coder
import numpy as np
from typing import Union, List

class VigenereCoder(coder.CipherCoder):
    
    def __init__(self, strKey: str, strXM: List[str]=lman.listAlpha(), strYM: List[str]=lman.listAlpha(), strGridM: np.ndarray=lman.listToNpGrid(lman.listAlpha()), bKeepUnknown: bool=True):
        
        self.strKey = re.sub(r'\s', '', strKey).upper()
        self.iKeyLen = len(self.strKey)
        self.strXM = strXM
        self.strYM = strYM
        self.strGridM = strGridM
        self.iLen = len(strXM)
        self.bKeepUnknown = True

        self.strXM = [ x.upper() for x in self.strXM ]
        self.strYM = [ y.upper() for y in self.strYM ]

        # ensure a user provided grid (may be a list) is in all caps
        for x in range(0, self.iLen):
            self.strGridM[x] = [ strGridM[x][y].upper() for y in range(0, self.iLen) ]

        # ensure a user provided list is turned into an np.ndarray
        self.strGridM = np.array(self.strGridM)
        
        if False == lman.isset(self.strXM):
            raise Exception('strXM is not a set')

        if False == lman.isset(self.strYM):
            raise Exception('strYM is not a set')

        if False == lman.similar(self.strXM, self.strYM):
            raise Exception('strXM and strYM do not contain the same elements')

        if False == set(self.strXM).issuperset(self.strKey):
            raise Exception('strXM is not a superset of strKey')

        if False == self.__isValidGrid():
            raise Exception('strGridM is not a valid Vigerene Square')

        if False == lman.similar(self.strXM, self.strGridM[0]):
            raise Exception('strXM and strGridM[0] do not contain the same elements')

        self.dictX = lman.listToIncDict(self.strXM)
        self.dictY = lman.listToIncDict(self.strYM)
        self.bKeepUnknown = True

    def __isValidGrid(self) -> bool:
        
        for i in range(1, self.iLen):
            if not lman.similar(self.strGridM[0], self.strGridM[i]):
                return False

        return True
    
    # override
    def encodeStr(self, strLine: str, strOutputFile: str=None) -> str:

        iKey = 0
        strEncoded = ''
        strLine = strLine.upper()

        for strLetter in strLine:
            
            if not strLetter in self.strXM:

                if True == self.bKeepUnknown:
                    strEncoded + strLetter

                continue

            iX = self.dictX[self.strKey[iKey]]
            iY = self.dictY[strLetter]
            strEncLetter = self.strGridM[iX, iY]
            strEncoded += strEncLetter

            iKey += 1
            if iKey == self.iKeyLen:
                iKey = 0

        # if writing result to output file
        if strOutputFile:
            with open(strOutputFile, 'w') as outputFile:
                outputFile.write(strEncoded)

        return strEncoded

    # override
    def decodeStr(self, strLine: str, strOutputFile: str=None) -> str:
        
        iKey = 0
        strDecoded = ''
        strLine = strLine.upper()

        for strLetter in strLine:
            
            if not strLetter in self.strXM:

                if True == self.bKeepUnknown:
                    strDecoded += strLetter

                continue
            
            strCol = self.strGridM[:, self.dictX[self.strKey[iKey]]]

            for i in range(0, self.iLen):
                if strLetter == strCol[i]:
                    iY = i
                    break

            strDecoded += self.strYM[iY]

            iKey += 1
            if iKey == self.iKeyLen:
                iKey = 0

        # if writing result to output file
        if strOutputFile:
            with open(strOutputFile, 'w') as outputFile:
                outputFile.write(strDecoded)

        return strDecoded
