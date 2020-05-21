#!/usr/bin/env python3

# Author: Christian Bargraser

# FUNCTIONS
#
# def encodeStr(strLine: str) -> str:
#     - Encode a string
#
# def decodeStr(strLine: str) -> str:
#     - Decode a string
#
# def encode(strInputFile: str, strOutputFile: str) -> None:
#     - Encode a file
#
# def decode(strInputFile: str, strOutputFile: str) -> None:
#     - Decode a file
#
# def tapcode(bEncode: bool, strInputFile: str, strOutputFile: str) -> None:
#     - Either encode or decode a file

import os

decodeDict = {
    
    '1,1' : 'A', 
    '1,2' : 'B', 
    '1,3' : 'C', # K
    '1,4' : 'D',
    '1,5' : 'E',
    '2,1' : 'F',
    '2,2' : 'G',
    '2,3' : 'H',
    '2,4' : 'I',
    '2,5' : 'J',
    '3,1' : 'L',
    '3,2' : 'M',
    '3,3' : 'N',
    '3,4' : 'O',
    '3,5' : 'P',
    '4,1' : 'Q',
    '4,2' : 'R',
    '4,3' : 'S',
    '4,4' : 'T',
    '4,5' : 'U',
    '5,1' : 'V',
    '5,2' : 'W',
    '5,3' : 'X',
    '5,4' : 'Y',
    '5,5' : 'Z'
}

encodeDict = {
    
    'A' : '1,1', 
    'B' : '1,2', 
    'C' : '1,3',
    'D' : '1,4',
    'E' : '1,5',
    'F' : '2,1',
    'G' : '2,2',
    'H' : '2,3',
    'I' : '2,4',
    'J' : '2,5',
    'K' : '1,3',
    'L' : '3,1',
    'M' : '3,2',
    'N' : '3,3',
    'O' : '3,4',
    'P' : '3,5',
    'Q' : '4,1',
    'R' : '4,2',
    'S' : '4,3',
    'T' : '4,4',
    'U' : '4,5',
    'V' : '5,1',
    'W' : '5,2',
    'X' : '5,3',
    'Y' : '5,4',
    'Z' : '5,5'
}

def encodeStr(strLine: str) -> str:
    
    strEncodedText = '' 

    bFirstLetter = True

    for strLetter in strLine:
        
        if strLetter.isspace():
            continue

        strEncodedLetter = encodeDict.get(strLetter.upper())

        if not strEncodedLetter:
            continue

        # if the character was not encoded (not in dict)
        if not strEncodedLetter:
            strEncodedLetter = strLetter

        if False == bFirstLetter:
            strEncodedLetter = '|' + strEncodedLetter

        else:
            bFirstLetter = False

        strEncodedText += strEncodedLetter
    
    return strEncodedText

def decodeStr(strLine: str, bProcessBadInput=False) -> str:

    strEncodedPairsM = strLine.split('|')
    strDecodedText = ''

    for strPair in strEncodedPairsM:

        strDecodedPair = decodeDict.get(strPair)

        # pair was not in decodeDict
        if not strDecodedPair:

            if True == bProcessBadInput:
                strDecodedPair = f'<?{strPair}?>'
            else:
                continue

        strDecodedText += strDecodedPair

    return strDecodedText

def encode(strInputFile: str, strOutputFile: str) -> None:
    coder(True, strInputFile, strOutputFile)

def decode(strInputFile: str, strOutputFile: str) -> None:
    coder(False, strInputFile, strOutputFile)

def coder(bEncode: bool, strInputFile: str, strOutputFile: str) -> None:
    
    if strOutputFile:
        outputFile = open(strOutputFile, 'w')

    inputFile = open(strInputFile, 'r')
    strLine = inputFile.readline().strip()

    while strLine:
        
        # encode
        if True == bEncode:
            strResult = encodeStr(strLine)

        # decode
        else:
            strResult = decodeStr(strLine)

        # write to file
        if strOutputFile:
            outputFile.write(strResult)
        
        # print to console
        else:
            print(strResult)

        strLine = inputFile.readline().strip()

    if strOutputFile:
        outputFile.close()