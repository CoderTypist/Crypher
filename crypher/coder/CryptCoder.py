#!/usr/bin/env python3

# Author: Christian Bargraser

# ABSTRACT METHODS
# ################
# 
# def encryptStr(self, strLine: str, iShift: int, strOutputFile: str=None) -> str:
#     - Encrypt a string
# 
# def decryptStr(self, strLine: str, iShift: int, strOutputFile: str=None) -> str:
#     - Decrypt a string
# 
# FUNCTIONS
# #########
# 
# def encrypteFile(self, strInputFile: str, iShift: int, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
#     - Encrypt a file
# 
# def decryptFile(self, strInputFile: str, iShift: int, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
#     - Decrypt a file
# 
# def cryptFile(self, bEncrypt: bool, strInputFile: str, iShift: int, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
#     - Either encrypt or decrypt a file
#     - bRetStr specifies whether the resulting string is created and returned.
#           Why enable and disable the returning of a String?
#           The result of each call to encryptFile/decryptFile will be appended to strCrypted.
#           This could result in a really string which may never be used.

from abc import ABC, abstractmethod
from typing import Union

class CryptCoder(ABC):

    @abstractmethod
    def encryptStr(self, strLine: str, strOutputFile: str=None) -> str:
        pass
    
    @abstractmethod
    def decryptStr(self, strLine: str, strOutputFile: str=None) -> str:
        pass

    def encryptFile(self, strInputFile: str, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
        return self.cryptFile(True, strInputFile, strOutputFile=strOutputFile, bRetStr=bRetStr)

    def decryptFile(self, strInputFile: str, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
        return self.cryptFile(False, strInputFile, strOutputFile=strOutputFile, bRetStr=bRetStr)

    def cryptFile(self, bEncrypt: bool, strInputFile: str, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
            
        with open(strInputFile, 'r') as inputFile:
            
            outputFile = None
            if None != strOutputFile:
                outputFile = open(strOutputFile, 'w')

            strCryptedText = ''
            strLine = inputFile.readline().rstrip()

            while strLine:
                
                # encrypting
                if True == bEncrypt:                  
                    strCryptedLine = self.encryptStr(strLine)

                # decrypting
                else:
                    strCryptedLine = self.decryptSt(strLine)

                # if writing to file
                if None != outputFile:
                    outputFile.write(strCryptedLine)

                # if returning string
                if True == bRetStr:
                    strCryptedText += strCryptedLine
                
                strLine = inputFile.readline().rstrip()
        
        if True == bRetStr:
            return strCryptedText