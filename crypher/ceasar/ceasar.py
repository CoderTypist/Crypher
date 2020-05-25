#!/usr/bin/env python3

# Author: Christian Bargraser

# INSTANCE ATTRIBUTES
# ###################
# 
# self.strAlphaM: list[str]
#     - Alphabet used by the ceasar cipher
#
# self.iLast: str
#     - Index of the last character in self.strAlphaM
# 
# self._iShift: int
#     - Number of times to shift a character along self.strAlphaM
#
# self.dictCipher: dict[str, int]
#     - Index for a letter in strAlphaM
#     - Instead of doing a linear search for a letter in strAlphaM, retrieve the index in O(1)
#     - key:str
#     - value: int
#
# self.bKeepUnknown: bool
#     - Keep characters that are not in self.strAlphaM
#
# self.bPrintShift: bool
#     - Prepend the number of shifts performed to the result
#
# FUNCTIONS
# #########
# 
# def __init__(self, strAlphaM: List[str]=lman.listAlpha(), bKeepUnknown: bool=True):
#     - strAlphaM is set to a list with 'A' to 'Z' inclusive
# 
# def __coderStr(self, bEncode: bool, strLine: str, iShift: int, strOutputFile: str=None) -> str:
#     - Either encode or decode a string
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

from .. import lman
from .. import coder
from typing import Union, List

class CeasarCoder(coder.CipherCoder):

    def __init__(self, iShift: int, strAlphaM: List[str]=lman.listAlpha(), bKeepUnknown: bool=True):
        
        self.strAlphaM = strAlphaM
        self.iLast = len(strAlphaM) - 1
        self.iShift = iShift
        self.dictCipher = lman.listToIncDict(self.strAlphaM)
        self.bKeepUnknown = True
        self.bPrintShift = False
    
    @property
    def iShift():
        return self._iShift

    @iShift.setter
    def iShift(self, iShift):
        self._iShift = abs(iShift) % self.iLast

    # override
    def encodeStr(self, strLine: str, strOutputFile: str=None) -> str:
        return self.__coderStr(True, strLine, strOutputFile=strOutputFile)

    # override
    def decodeStr(self, strLine: str, strOutputFile: str=None) -> str:
        return self.__coderStr(False, strLine,strOutputFile=strOutputFile)

    def __coderStr(self, bEncode: bool, strLine: str, strOutputFile: str=None) -> str:
        
        strLine = strLine.upper()
        strCoded = ''

        for strLetter in strLine:
            
            # skip non-alphabetic characters
            if not strLetter.isalpha():
                
                if True == self.bKeepUnknown:
                    strCoded += strLetter

                continue

            iLetterIndex = self.dictCipher.get(strLetter)
            
            for i in range(0, self._iShift):
                
                # encode
                if True == bEncode:

                    if self.iLast == iLetterIndex:
                        iLetterIndex = 0

                    else:
                        iLetterIndex += 1

                # decode
                else:
                    if 0 == iLetterIndex:
                        iLetterIndex = self.iLast

                    else:
                        iLetterIndex -= 1

            strCoded += self.strAlphaM[iLetterIndex]
        
        if True == self.bPrintShift:
            strCoded = f'{self._iShift:<2} ' + strCoded

        # if writing result to output file
        if strOutputFile:
            with open(strOutputFile, 'w') as outputFile:
                outputFile.write(strEncoded)

        return strCoded