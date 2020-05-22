#!/usr/bin/env python3

# Author: Christian Bargraser

# FUNCTIONS
#
# def addCipherArgs(parser: argparse.ArgumentParser) -> None:
#     - Add base arguments for encoding/decoding
# 
# def addCryptArgs(parser: argparse.ArgumentParser) -> None:
#     - Add base arguments for encrypting/decrypting
#
# def isEncodeToConsole(dictArgs: dict) -> bool:
#     - Return True if encoding the input and printing the output to the console
#
# def isDecodeToConsole(dictArgs: dict) -> bool:
#     - Return True if decoding the input and printing the output to the console
#
# def isEncodeToFile(dictArgs: dict) -> bool:
#     - Return True if encoding the input and writing the output to a file
# 
# def isDecodeToFile(dictArgs: dict) -> bool:
#     - Return True if decoding the input and writing the output to a file

import argparse

def addCipherArgs(parser: argparse.ArgumentParser) -> None:

    group_action = parser.add_mutually_exclusive_group(required=True)
    group_action.add_argument('-e', '--encode', action='store_true', help='plaintext file')
    group_action.add_argument('-d', '--decode', action='store_true', help='encoded file')
    
    group_input = parser.add_mutually_exclusive_group(required=True)
    group_input.add_argument('-t', '--text', help='input text')
    group_input.add_argument('-i', '--input', help='input file')

    parser.add_argument('-o', '--output', help='output file')

def addCryptArgs(parser: argparse.ArgumentParser) -> None:

    group_action = parser.add_mutually_exclusive_group(required=True)
    group_action.add_argument('-e', '--encrypt', action='store_true', help='plaintext file')
    group_action.add_argument('-d', '--decrypt', action='store_true', help='encrypted file')
    
    group_input = parser.add_mutually_exclusive_group(required=True)
    group_input.add_argument('-t', '--text', help='input text')
    group_input.add_argument('-i', '--input', help='input file')

    parser.add_argument('-o', '--output', help='output file')

def isEncodeToConsole(dictArgs: dict) -> bool:
    return True == dictArgs.get('encode') and None == dictArgs.get('output')

def isDecodeToConsole(dictArgs: dict) -> bool:
    return True == dictArgs.get('decode') and None == dictArgs.get('output')

def isEncodeToFile(dictArgs: dict) -> bool:
    return True == dictArgs.get('encode') and None != dictArgs.get('output')

def isDecodeToFile(dictArgs: dict) -> bool:
    return True == dictArgs.get('decode') and None != dictArgs.get('output')
    