#!/usr/bin/env python3

# Author: Christian Bargraser

# def __isValidGrid(self):
#     - Return True if self.strGridM is a valid Vigerene Square, False otherwise
#     - Ensures all rows have the same elements
#     - Ensures that all rows are the same length

import re
from .. import lman
import numpy as np
from typing import Union, List

class VigenereCoder:
    
    def __init__(self, strKey: str, strXM: List[str]=lman.listAlpha(), strYM: List[str]=lman.listAlpha(), strGridM: np.ndarray=lman.listToNpGrid(lman.listAlpha())):
        
        self.strKey = re.sub(r'\s', '', strKey)
        self.strXM = strXM
        self.strYM = strYM
        self.strGridM = strGridM
        self.iLast = len(strXM) - 1

        if False == lman.isset(strXM):
            raise Exception('strXM is not a set')

        if False == lman.isset(strYM):
            raise Exception('strYM is not a set')

        if False == lman.similar(strXM, strYM):
            raise Exception('strXM and strYM do not contain the same elements')

        if False == self.__isValidGrid():
            raise Exception('strGridM is not a valid Vigerene Square')

        self.dictX = lman.listToIncDict(self.strXM)
        self.dictY = lman.listToIncDict(self.strYM)
        self.bKeepUnknown = True

    def __isValidGrid(self):
        
        for i in range(1, self.iLast):
            if not lman.similar(self.strGridM[0], self.strGridM[i])
                return False

        return True

    def encodeStr(self, strLine: str, strOutputFile: str=None) -> str:
        pass

    def decodeStr(self, strLine: str, strOutputFile: str=None) -> str:
        pass

    def encodeFile(self, strInputFile: str, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
        pass

    def decodeFile(self, strInputFile: str, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
        pass

    def coderFile(self, bEncode: bool, strInputFile: str, strOutputFile: str=None, bRetStr: bool=True) -> Union[str,None]:
        pass