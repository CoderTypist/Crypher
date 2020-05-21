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
# def listToGrid(arr: list) -> list:
#     - Returns a 2-dimensional list
#     - Dimensions: len(arr) x len(arr)
#     - Each row is rotated to the right <row#/index#> times
#
# def printGrid(grid: list) -> None:
#     - Prints each row in the grid on its own line

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
    for i in range(0, abs(iRot)):

        if iRot < 0:
            arr = arr[1:] + list(arr[0])

        else:
            arr = list(arr[iLast]) + arr[0:iLast]

    return arr

def listToGrid(arr: list) -> list:
    
    if not arr:
        return arr

    grid = []
    for i in range(0, len(arr)):
        grid.append(rot(arr, -i))

    return grid

def printGrid(grid: list) -> None:

    for subList in grid:
        print(subList)