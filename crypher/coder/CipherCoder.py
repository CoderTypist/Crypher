#!/usr/bin/env python3

# Author: Christian Bargraser

# ABSTRACT METHODS
# ################
# 
# def encodeStr(self, strLine: str, iShift: int, strOutputFile: str=None) -> str:
#     - Encode a string
# 
# def decodeStr(self, strLine: str, iShift: int, strOutputFile: str=None) -> str:
#     - Decode a string
# 
# FUNCTIONS
# #########
# 
# def encodeFile(self, strInputFile: str, iShift: int, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
#     - Encode a file
# 
# def decodeFile(self, strInputFile: str, iShift: int, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
#     - Decode a file
# 
# def coderFile(self, bEncode: bool, strInputFile: str, iShift: int, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
#     - Either encode or decode a file
#     - bRetStr specifies whether the resulting string is created and returned.
#           Why enable and disable the returning of a String?
#           The result of each call to encodeFile/decodeFile will be appended to strEncoded.
#           This could result in a really string which may never be used.

from abc import ABC, abstractmethod
from typing import Union

class CipherCoder(ABC):

    @abstractmethod
    def encodeStr(self, strLine: str, strOutputFile: str=None) -> str:
        pass
    
    @abstractmethod
    def decodeStr(self, strLine: str, strOutputFile: str=None) -> str:
        pass

    def encodeFile(self, strInputFile: str, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
        return self.coderFile(True, strInputFile, strOutputFile=strOutputFile, bRetStr=bRetStr)

    def decodeFile(self, strInputFile: str, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
        return self.coderFile(False, strInputFile, strOutputFile=strOutputFile, bRetStr=bRetStr)

    def coderFile(self, bEncode: bool, strInputFile: str, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
            
        with open(strInputFile, 'r') as inputFile:
            
            outputFile = None
            if None != strOutputFile:
                outputFile = open(strOutputFile, 'w')

            strCodedText = ''
            strLine = inputFile.readline().rstrip()

            while strLine:
                
                # encode
                if True == bEncode:                  
                    strCodedLine = self.encodeStr(strLine)

                # decode
                else:
                    strCodedLine = self.decodeStr(strLine)

                # if writing to file
                if None != outputFile:
                    outputFile.write(strCodedLine)

                # if returning string
                if True == bRetStr:
                    strCodedText += strCodedLine
                
                strLine = inputFile.readline().rstrip()
        
        if True == bRetStr:
            return strCodedText