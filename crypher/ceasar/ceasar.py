#!/usr/bin/env python3

# Author: Christian Bargraser

# FUNCTIONS
#
# def encodeStr(strLine: str, iShift: int, bKeepPunctuation=False) -> str:
#     - Encode a string
#
# def decodeStr(strLine: str, iShift: int, bKeepPunctuation=False) -> str:
#     - Decode a string
#
# def encode(strInputFile: str, strOutputFile: str, iShift: int) -> None:
#     - Encode a file
#
# def decode(strInputFile: str, strOutputFile: str, iShift: int) -> None:
#     - Decode a file
#
# def ceasarcode(bEncode: bool, strInputFile: str, strOutputFile: str, iShift: int) -> None:
#     - Either encode or decode a file

def encodeStr(strLine: str, iShift: int, bKeepNonAlpha=True) -> str:
    
    strLine = strLine.upper()
    strEncoded = ''

    for strLetter in strLine:
        
        # skip non-alphabetic characters
        if not strLetter.isalpha():

            if True == bKeepNonAlpha:
                strEncoded += strLetter

            continue

        for i in range(0, abs(iShift)):

            if 'Z' == strLetter:
                strLetter = 'A'

            else:
                strLetter = chr(ord(strLetter)+1)

        strEncoded += strLetter
    
    return strEncoded

def decodeStr(strLine: str, iShift: int, bKeepNonAlpha=True) -> str:

    strLine = strLine.upper()
    strEncoded = ''

    for strLetter in strLine:
        
        # skip non-alphabetic characters
        if not strLetter.isalpha():
            
            if True == bKeepNonAlpha:
                strEncoded += strLetter

            continue

        for i in range(0, abs(iShift)):

            if 'A' == strLetter:
                strLetter = 'Z'

            else:
                strLetter = chr(ord(strLetter)-1)

        strEncoded += strLetter
    
    return strEncoded

def encode(strInputFile: str, strOutputFile: str, iShift: int) -> None:
    coder(True, strInputFile, strOutputFile, iShift)

def decode(strInputFile: str, strOutputFile: str, iShift: int) -> None:
    coder(False, strInputFile, strOutputFile, iShift)

def coder(bEncode: bool, strInputFile: str, strOutputFile: str, iShift: int) -> None:
        
    if strOutputFile:
        outputFile = open(strOutputFile, 'w')

    inputFile = open(strInputFile, 'r')
    strLine = inputFile.readline().strip()

    while strLine:
        
        # encode
        if True == bEncode:
            strResult = encodeStr(strLine, iShift)

        # decode
        else:
            strResult = decodeStr(strLine, iShift)

        # write to file
        if strOutputFile:
            outputFile.write(strResult, iShift)
        
        # print to console
        else:
            print(strResult)

        strLine = inputFile.readline().strip()

    if strOutputFile:
        outputFile.close()