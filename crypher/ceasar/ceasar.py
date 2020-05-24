#!/usr/bin/env python3

# Author: Christian Bargraser

# INSTANCE ATTRIBUTES
#####################
# 
# self.strAlphaM: list[str]
#     - Alphabet used by the ceasar cipher
#
# self.iLast: str
#     - Index of the last character in self.strAlphaM
# 
# self.dictCipher: dict[str, int]
#     - Index for a letter in strAlphaM
#     - Instead of doing a linear search for a letter in strAlphaM, retrieve the index in O(1)
#     - key:str
#     - value: int
#
# self.bKeepNonAlpha: bool
#     - Keep characters that are not letters
#
# self.bPrintShift: bool
#     - Include the number of shifts performed in the result
#
# FUNCTIONS
###########
# 
# def __init__(self, strAlphaM=lman.listAlpha(), bKeepNonAlpha=True):
#     - Create new instance of CeasarCoder
#     - strAlphaM is set to a list with 'A' to 'Z' inclusive
#     - strAlphaM allows the CeasarCoder to have a different alphabet
# 
# def encodeStr(self, strLine: str, iShift: int, strOutputFile=None) -> str:
#     - Encode a string
#     - Invokes coderStr()
# 
# def decodeStr(self, strLine: str, iShift: int, strOutputFile=None) -> str:
#     - Decode a string
#     - Invokes coderStr()
# 
# def coderStr(self, bEncode: bool, strLine: str, iShift: int, strOutputFile=None) -> str:
#     - Either encode or decode a string
#     - Has the option to save output to a file
# 
# def encodeFile(self, strInputFile: str, iShift: int, strOutputFile=None, bRetStr=True) -> Union[str,None]:
#     - Encode a file
#     - Invokes coderFile()
# 
# def decodeFile(self, strInputFile: str, iShift: int, strOutputFile=None, bRetStr=True) -> Union[str,None]:
#     - Decode a file
#     - Invokes coderFile()
# 
# def coderFile(self, bEncode: bool, strInputFile: str, iShift: int, strOutputFile=None, bRetStr=True) -> Union[str,None]:
#     - Either encode or decode a file
#     - bRetStr specifies whether the resulting string is created and returned.
#           Why enable and disable the returning of a String?
#           The result of each call to encodeFile/decodeFile will be appended to strEncoded.
#           This could result in a really string which may never be used.

from .. import lman
from typing import Union

class CeasarCoder:

    def __init__(self, strAlphaM=lman.listAlpha(), bKeepNonAlpha=True):

        self.strAlphaM = strAlphaM
        self.iLast = len(strAlphaM) - 1
        self.dictCipher = {}
        self.bKeepNonAlpha = True
        self.bPrintShift = False

        i = 0
        for strLetter in self.strAlphaM:
            self.dictCipher[strLetter] = i
            i = i+1
    
    def encodeStr(self, strLine: str, iShift: int, strOutputFile=None) -> Union[str,None]:
        return self.coderStr(True, strLine, iShift, strOutputFile=strOutputFile)

    def decodeStr(self, strLine: str, iShift: int, strOutputFile=None) -> Union[str,None]:
        return self.coderStr(False, strLine, iShift, strOutputFile=strOutputFile)

    def coderStr(self, bEncode: bool, strLine: str, iShift: int, strOutputFile=None) -> Union[str,None]:
        
        iShift = iShift % self.iLast
        strLine = strLine.upper()
        strEncoded = ''

        for strLetter in strLine:
            
            # skip non-alphabetic characters
            if not strLetter.isalpha():
                
                if True == self.bKeepNonAlpha:
                    strEncoded += strLetter

                continue

            iLetterIndex = self.dictCipher.get(strLetter)
            
            for i in range(0, abs(iShift)):
                
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

            strEncoded += self.strAlphaM[iLetterIndex]
        
        if True == self.bPrintShift:
            strEncoded = f'{iShift:<2} ' + strEncoded

        # if writing result to output file
        if strOutputFile:
            with open(strOutputFile, 'w') as outputFile:
                outputFile.write(strEncoded)

        return strEncoded

    def encodeFile(self, strInputFile: str, iShift: int, strOutputFile=None, bRetStr=True) -> Union[str,None]:
        return self.coderFile(True, strInputFile, iShift, strOutputFile=strOutputFile, bRetStr=bRetStr)

    def decodeFile(self, strInputFile: str, iShift: int, strOutputFile=None, bRetStr=True) -> Union[str,None]:
        return self.coderFile(False, strInputFile, iShift, strOutputFile=strOutputFile, bRetStr=bRetStr)

    def coderFile(self, bEncode: bool, strInputFile: str, iShift: int, strOutputFile=None, bRetStr=True) -> Union[str,None]:
            
        with open(strInputFile, 'r') as inputFile:
            
            outputFile = None
            if None != strOutputFile:
                outputFile = open(strOutputFile, 'w')

            strEncoded = ''
            strLine = inputFile.readline()

            while strLine:
                
                # encode
                if True == bEncode:                  
                    strCoded = self.encodeStr(strLine, iShift)

                # decode
                else:
                    strCoded = self.decodeStr(strLine, iShift)

                # if writing to file
                if None != outputFile:
                    outputFile.write(strCoded)

                # if returning string
                if True == bRetStr:
                    strEncoded += strCoded
                
                strLine = inputFile.readline()
        
        if True == bRetStr:
            return strEncoded
