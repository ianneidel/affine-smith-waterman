#!/usr/bin/python
__author__ = "Ian Neidel"
__email__ = "ian.neidel@yale.edu"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = "1.0.0"

### Usage: python hw1.py -i <input file> -s <score file>
### Example: python hw1.py -i input.txt -s blosum62.txt
### Note: Smith-Waterman Algorithm

DIAGONAL = 0
ABOVE = 1
LEFT = 2

import argparse
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser(description='Smith-Waterman Algorithm')
parser.add_argument('-i', '--input', help='input file', required=True)
parser.add_argument('-s', '--score', help='score file', required=True)
parser.add_argument('-o', '--opengap', help='open gap', required=False, default=-2)
parser.add_argument('-e', '--extgap', help='extension gap', required=False, default=-1)
args = parser.parse_args()

def extractSequences(inputFile):
    with open(inputFile, "r") as f:
        input = f.read()
        splitInput = input.split("\n")
        return splitInput[0],splitInput[1]
    
def addHeaders(scoreMatrix, s1, s2):
    newScoreMatrix = np.empty((scoreMatrix.shape[0]+1,scoreMatrix.shape[1]+1,2),dtype=object)
    newScoreMatrix[1:,1:] = scoreMatrix.astype(str)
    newScoreMatrix[2:,0,0] = [str(el) for el in s1]
    newScoreMatrix[0,2:,0] = [str(el) for el in s2]
    return newScoreMatrix

def traceback(s1,s2,scoreMatrix):
    justScores = scoreMatrix[:,:,0]
    besti,bestj = np.unravel_index(justScores.argmax(), justScores.shape)
    bestScore = justScores[besti,bestj]
    if bestScore == 0:
        return "","","",0
    i,j = besti,bestj
    s1endlen = len(s1[i:])
    s2endlen = len(s2[j:])
    s1align = ")" + " " * max(s2endlen-s1endlen,0)
    if i < len(s1):
        s1align = s1align+s1[i:]
    alignLines = " " * max(s1endlen+1,s2endlen+1)
    s2align = ")" + " " * max(s1endlen-s2endlen,0)
    if j < len(s2):
        s2align = s2align+s2[j:]
    while True:
        if justScores[i,j] == 0:
            break
        tracer = scoreMatrix[i,j,1]
        move = int(tracer) % 3
        distance = int(tracer) // 3
        if move == DIAGONAL:
            s1val = s1[i-1]
            s2val = s2[j-1]
            s1align = s1val+s1align
            s2align = s2val+s2align
            alignChar = "|" if s1val == s2val else " "
            alignLines = alignChar+alignLines
            i-=1; j-=1
        elif move == LEFT:
            s1align = "-"*distance + s1align
            alignLines = " "*distance + alignLines
            s2align = s2[j-distance:j]+s2align
            j-=distance
        elif move == ABOVE:
            s1align = s1[i-distance:i]+s1align
            alignLines = " "*distance + alignLines
            s2align = "-"*distance + s2align
            i-=distance
    
    s1start = s1[:i]
    s2start = s2[:j]
    s1align = " " * max(len(s2start)-len(s1start),0) + s1start + "(" + s1align
    s2align = " " * max(len(s1start)-len(s2start),0) + s2start + "(" + s2align
    alignLines = " " * (max(len(s2start),len(s1start))+1) + alignLines
    
    return s1align, alignLines, s2align, bestScore

def explainMove(tracer):
    if tracer == None:
        return "-"
    move = int(tracer) % 3
    distance = int(tracer) // 3
    if move == LEFT:
        movetxt = "left"
    elif move == ABOVE:
        movetxt = "above"
    else:
        movetxt = "diag"
    return f"{movetxt}{str(distance)}"

def printScoreMatrix(s1,s2,scoreMatrix):
    headerScoreMatrix = addHeaders(scoreMatrix, s1, s2)
    for row in headerScoreMatrix.transpose((1,0,2)):
        rowVals = [f"{el[0],explainMove(el[1])}" if el[0] is not None else "" for el in row]
        tabbedRow = "\t".join(rowVals)
        print(tabbedRow+"\t")

def printAlgOutput(s1,s2,scoreMatrix):
    print("-----------\n|Sequences|\n-----------")
    print(f"sequence1\n{s1}")
    print(f"sequence2\n{s2}")
    print("--------------\n|Score Matrix|\n--------------")
    headerScoreMatrix = addHeaders(scoreMatrix, s1, s2)
    for row in headerScoreMatrix.transpose((1,0,2)):
        rowVals = [el[0] if el[0] is not None else "" for el in row]
        tabbedRow = "\t".join(rowVals)
        print(tabbedRow+"\t")
    print("----------------------\n|Best Local Alignment|\n----------------------")
    s1align, alignLines, s2align, bestScore = traceback(s1,s2,scoreMatrix)
    print(f"Alignment Score:{bestScore}")
    print(f"Alignment Results:\n{s1align}\n{alignLines}\n{s2align}")

def getScore(i,j,scoreMatrix):
    return scoreMatrix[i,j,0]

def findBestMove(diag,above,vertjump,left,horizjump):
    if diag == max(diag,above,left):
        return DIAGONAL
    elif above == max(diag,above,left):
        return ABOVE+3*vertjump
    else:
        return LEFT+3*horizjump

def genVertScore(scoreMatrix,i,j,openGap,extGap):
    max, jumpsize = -np.inf, 0
    k = 1
    while i-k >= 0:
        val = getScore(i-k,j,scoreMatrix)+openGap+extGap*(k-1)
        if val > max:
            max, jumpsize = val, k
        k+=1
    return max, jumpsize

def genHorizScore(scoreMatrix,i,j,openGap,extGap):
    max, jumpsize = -np.inf, 0
    k = 1
    while j-k >= 0:
        val = getScore(i,j-k,scoreMatrix)+openGap+extGap*(k-1)
        if val > max:
            max, jumpsize = val, k
        k+=1
    return max, jumpsize

def setMaxScore(i,j,scoreMatrix,s1,s2,similarityDict,openGap,extGap):
    matchScore = similarityDict[s1[i-1]][s2[j-1]]
    diag = getScore(i-1,j-1,scoreMatrix)+matchScore
    above, vertjump = genVertScore(scoreMatrix,i,j,openGap,extGap)
    left, horizjump = genHorizScore(scoreMatrix,i,j,openGap,extGap)
    
    # set score for cell
    scoreMatrix[i,j,0] = max(diag,above,left,0)
    scoreMatrix[i,j,1] = findBestMove(diag,above,vertjump,left,horizjump)
        

### Implement your Smith-Waterman Algorithm
def runSW(inputFile, scoreFile, openGap, extGap):
    s1,s2 = extractSequences(inputFile)
    similarityDict = pd.read_csv(scoreFile, delim_whitespace=True).to_dict()

    n,m = len(s1)+1,len(s2)+1
    scoreMatrix = np.zeros((n,m,2),dtype=np.int64)
    
    for i in range(1,n):
        for j in range(1,m):
            setMaxScore(i,j,scoreMatrix,s1,s2,similarityDict,openGap,extGap)

    printAlgOutput(s1,s2,scoreMatrix)
    # printScoreMatrix(s1,s2,scoreMatrix)
    

### Run your Smith-Waterman Algorithm
runSW(args.input, args.score, args.opengap, args.extgap)