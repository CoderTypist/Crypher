#!/usr/bin/env python3

# Author: Christian Bargraser

# FUNCTIONS
#
# def listAlpha() -> list:
#     - Returns a list containing the alphabet (uppercase)
# 
# def listLowerAlpha() -> list:
#     - Returns a list containing the alphabet (lowercase)
#
# def listUpperAlpha() -> list:
#     - Returns a list containing the alphabet (uppercase)
#
# def rot(arr: list, iRot: int) -> list:
#     - Rotates the list iRot times
#     - If iRot is positive, the list is rotated to the right
#     - If iRot is negative, the list is rotates to the left
#
# def listToListGrid(arr: list) -> list:
#     - Returns a 2-dimensional list
#     - Dimensions: len(arr) x len(arr)
#     - Each row is rotated to the right <row#/index#> times
#
# def printListGrid(grid: list) -> None:
#     - Prints each row in the grid on its own line
#
# def listToNpGrid(arr: list) -> list:
#     - Returns an 2-dimensional np.array()
#     - Dimensions: len(arr) x len(arr) 
#     - Each row is rotated to the right <row#/index#> times
#     - Grid is initially created by calling listToListGrid()
#
# def def listToIncDict(arr: list) -> dict:
#     - Returns a dictionary created from the list
#     - The keys are the values from the list
#     - The values are assigned incrementally starting from 0
#
# def isset(arr: list) -> bool:
#     - Returns True if arr is a set, otherwise False is returned
#
# def similar(arrOne: list, arrTwo: list) -> bool:
#     - Returns True if arrOne and arrTWo contain the same elements, otherwise False is returned

import numpy as np

def listAlpha() -> list:
    return [chr(x) for x in range(ord('A'), ord('Z')+1)]

def listLowerAlpha() -> list:
    return [chr(x) for x in range(ord('a'), ord('z')+1)]

def listUpperAlpha() -> list:
    return listAlpha()

def rot(arr: list, iRot: int) -> list:
    
    if not list or 0 == iRot:
        return arr

    iLast = len(arr) - 1

    # len(arr) == 1
    if 0 == iLast:
        return arr

    for i in range(0, abs(iRot)):

        if iRot < 0:
            arr = arr[1:] + list(arr[0])

        else:
            arr = list(arr[iLast]) + arr[0:iLast]

    return arr

def listToListGrid(arr: list) -> list:
    
    if None == arr:
        return arr

    grid = []
    for i in range(0, len(arr)):
        grid.append(rot(arr, -i))

    return grid

def printListGrid(grid: list) -> None:

    for subList in grid:
        print(subList)

def listToNpGrid(arr: list) -> list:
    return np.array(listToListGrid(arr))    

def listToIncDict(arr: list) -> dict:

    if None == arr:
        return arr

    arrDict = {}
    i = 0

    for item in arr:
        arrDict[item] = i
        i += 1

    return arrDict

def isset(arr: list) -> bool:

    if None == arr:
        return False

    return len(arr) == len(set(arr))

def similar(arrOne: list, arrTwo: list) -> bool:
    return arrOne.copy().sort() == arrTwo.copy().sort()