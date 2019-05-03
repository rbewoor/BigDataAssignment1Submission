"""
# -*- coding: utf-8 -*-
# 28 April 2019
# Big Data Programming - Assignment 1 - Problem 1: Find longest common subsequence for two strings provided
#   Input strings to be evaluated with following conditions: only lowercase alphabetic allowed, no spaces or special characters
#   Example:
#   Inputs:                 String1 = "ABAZDC"           String2 = "BACBAD"
#   Expected output:        "ABAD"
#
#   Program will show one or more longest commmon sub-sequences, a count of the number of such sequences found and the value
#   of the length of the longest common sub-sequence.
#   This will be done separately for cases of sub-sequences being repeated and for without repetition (if applicable).
#
"""
#
##
####            function definitions start
##
#
def f1_remove_multiple_char_occurrences_from_string(inS):
    """ Returns a string while retaining only the first occurrence of each unique character found in the input string
    Input parameters:
        inS: the input string
    Output parameters:
        outS: the output string

    Example   input  = "ababcbskmdk"
    will have output = "abcskmd"
    """
    outS = ""
    for i in range( 0, len(inS) ):
        if (inS[i] != " "):
            outS = outS + inS[i]
            inS = inS.replace(inS[i]," ")
    return outS

def f2_find_NthOccurrence_of_char(withinStr, targetChar, N):
    """ Returns the position of the nth occurence of a target character in a string to be searched in
    Input parameters:
        withinStr: the string within which we want to find the Nth occurence of the target character
        targetChar: the character to be found
        N: the value for the Nth occurence number to be located
    Output parameters:
        ans: the position number of the Nth occurence. Value will be -1 if the Nth occurence does not exist

        Example   withinStr  = "bacadgaefgah"  ,  targetChar = "a"
                  N = 1   will have   output  ans = 1
                  N = 2   will have   output  ans = 3
                  N = 3   will have   output  ans = 6
                  N = 4   will have   output  ans = 10
                  N = 5   will have   output  ans = -1
    """
    if N > withinStr.count(targetChar):
        return(-1)
    occNo = 0
    for i in range(0, len(withinStr)):
        if withinStr[i: i+1] == targetChar:
            occNo = occNo + 1
        if occNo == N:
            return(i)

def f3_make_combos_all_length_specified(ipStr, lenIpStr, wantedLen, startPosForLoop, endPosForLoop, funcCallCount, strBuild):
    """ Takes a string as input and finds all possible sub-sequences of a certain length (while maintaing the original order).
        Note:       RECURSIVE calling done to complete the task and therefore requires the input parameters to be very
                    to be carefully provided in a very precise way to work.
        IMPORTANT:  The sequences are populated into a GLOBAL VARIABLE. So be sure to RESET this variable before calling each time
                    as required
    Input parameters:
        ipStr:              the input string of which the various sub sequences are to be identified
        lenIpStr:           the length of the input string
        wantedLen:          the length of the sub-sequences that should be identified
        startPosForLoop:    specify as zero when calling   i.e.  = 0
        endPosForLoop:      must be set to a value   =   length of input string  -  wanted length  +  1
        funcCallCount:      must match the wanted length value (wantedLen)
        strBuild:           set as a blank string while calling i.e. =   ""
    Output parameters:
        Does NOT EXPLICITY RETURN a value. But populates a GLOBAL VARIABLE called f3FuncOpList

    Example of a call from user logic point in application - make sure to populate all the variables as specified above:
         f3_make_combos_all_length_specified(workS2, len(workS2), wantedLen, 0, ( len(workS2)-wantedLen+1 ) , funcCallCount, "")

    Examples:
        Input string = "12345", wantedLength = 3
        Output list populated exactly in this order:
            [ "123" , "124" ,  "125" ,  "234" ,  "235" ,  "345" ]
        Input string = "123456", wantedLength = 4
        Output list populated exactly in this order:
            [ "1234" , "1235" ,  "1236" ,  "2345" ,  "2346" ,  "3456" ]
    """
#
#    Wanting to make generic to execute as many FOR loops as required depending on the wantedLen passed to function.
#           The commented code below is hard coded with only 3 FOR loops and thus can handle identifying sub-sequences
#           of 3 character length. By ensuring only one FOR loop is built for each function call, and then calling
#           the function again for each successive FOR loop build up, we achieve exactly the same logic as in the
#           commented reference code below.
#######  START of commented code for refernce
#    for i in range (0, lenIpStr-wantedLen+1):
#        for j in range(i+1, lenIpStr-wantedLen+2):
#            for k in range(j+1, lenIpStr-wantedLen+3):
#                #print( (s1[i] + s1[j] + s1[k] ) )
#                opList.append(ipStr[i] + ipStr[j] + ipStr[k])
#    return(opList)
#######  END   of commented code for refernce
#
    global f3FuncOpList
    #print("\nEntered the function f3")
    #print("funcCallCount= ",funcCallCount, "ipStr= ",ipStr, "wantedLen= ",wantedLen,    \
    #      "startPosForLoop= ",startPosForLoop, "endPosForLoop= ",endPosForLoop, "strBuild= ",strBuild)
    for i in range (startPosForLoop, endPosForLoop):
    #    print("\nEntered the FOR LOOP")
        strBuild = strBuild + ipStr[i:i+1]
    #    print("strBuild= ",strBuild)
        if funcCallCount == 0:
            return("PROBLEM....PROBLEM...should never have reached funcCallCount=0 position")
        if funcCallCount == 1:
            f3FuncOpList.append(strBuild)
        else:
            #print("\nRECURSIVE CALL to function")
            f3_make_combos_all_length_specified(ipStr, lenIpStr, wantedLen, i+1, endPosForLoop+1, funcCallCount-1, strBuild)
        strBuild = strBuild[:len(strBuild)-1]
    funcCallCount = funcCallCount + 1
    return()
#
##
####            function definitions ended
##
#
#
##
####            main program logic starts
##
#
# two hard coded strings as input
#origIpS1 = "dca bfadimac v bacsa a"
#origIpS2 = "  arbaf tvdcbq aa"
#origIpS1 = "werwgjioretksrel"
#origIpS2 = "reubnert"

# take inputs from console
origIpS1 = input("Please enter string 1: ")
origIpS2 = input("Please enter string 2: ")

workS1 = origIpS1
workS2 = origIpS2

# convert all strings to lowercase and then remove leading and trailing spaces
workS1 = workS1.lower()
workS2 = workS2.lower()
workS1 = workS1.strip()
workS2 = workS2.strip()

# handle whitespaces or new lines (that are inside the string) etc to create one continous string of valid characters
# https://stackoverflow.com/questions/3739909/how-to-strip-all-whitespace-from-string
workS1 = "".join(workS1.split())
workS2 = "".join(workS2.split())

# use the function call to get rid off multiple character occurrences first, then
# create a set of all unique characters presents in the two input strings
intersectionSetChars = set ( f1_remove_multiple_char_occurrences_from_string(workS1) )  &   \
                     set( f1_remove_multiple_char_occurrences_from_string(workS2) )

# clean the two strings to retain only characters that are present in both strings
#       (i.e. retain the intersection set characters present in each input string)
# only these will be used next for the actual subsequence finding logic
intersectionSetCharsString = "".join(intersectionSetChars)
for i in range(0, len(workS1) ):
    if ( intersectionSetCharsString.find(workS1[i]) == -1 ):
        workS1 = workS1.replace(workS1[i]," ")
workS1 = "".join(workS1.split())

for i in range(0, len(workS2) ):
    if ( intersectionSetCharsString.find(workS2[i]) == -1 ):
        workS2 = workS2.replace(workS2[i]," ")
workS2 = "".join(workS2.split())

# watn to keep workS1 as the shorter string
if len(workS1) != len(workS2):
    if len(workS1) > len(workS2):
        tempStr = workS2
        workS2 = workS1
        workS1 = tempStr

print(f"Original input strings:\norigIpS1 ==>{origIpS1}<==\norigIpS2 ==>{origIpS2}<==")
print(f"\nCleaned strings after removing leading, trailing, internal spaces; then treating S1 as shorter string" + " (if possible).")
print(f"workS1 ==>{workS1}<==\nworkS2 ==>{workS2}<==")

#
##  the actual main logic to find the longest common sub sequence start now
#
flagLongestSeqFound = 0
finalLongestCommonSubSeqs = []

wantedLen = len(workS1)             # at start we want to search for the longest possible string i.e. spanning all of workS1

while flagLongestSeqFound == 0 and wantedLen > 0:
    funcCallCount = wantedLen

    f3FuncOpList = []
    f3_make_combos_all_length_specified(workS1, len(workS1), wantedLen, 0, ( len(workS1)-wantedLen+1 ) , funcCallCount, "")
    s1_f3FuncOpList = f3FuncOpList.copy()
    f3FuncOpList = []
    f3_make_combos_all_length_specified(workS2, len(workS2), wantedLen, 0, ( len(workS2)-wantedLen+1 ) , funcCallCount, "")
    s2_f3FuncOpList = f3FuncOpList.copy()
    
    if len(s1_f3FuncOpList) > 0:
        for eachS1f3SubSeq in s1_f3FuncOpList:
            if eachS1f3SubSeq in s2_f3FuncOpList:
                flagLongestSeqFound = 1
                finalLongestCommonSubSeqs.append(eachS1f3SubSeq)
    wantedLen = wantedLen - 1       # start searching for shortened sub sequences from workS1 string

# sort the output list
finalLongestCommonSubSeqs.sort()

# check to see if there are repetitions of the sub-sequences found.
if ( len(finalLongestCommonSubSeqs) > 0):
    finalLongestCommonSubSeqsWithoutRep = []
    flagRepeatingElementsFound = False
    i = 0
    while i < len(finalLongestCommonSubSeqs):
        finalLongestCommonSubSeqsWithoutRep.append(finalLongestCommonSubSeqs[i])
        countCurrentElement = finalLongestCommonSubSeqs.count(finalLongestCommonSubSeqs[i])
        if countCurrentElement > 1:
            i = i + countCurrentElement
            flagRepeatingElementsFound = True
        else:
            i = i + 1

if flagLongestSeqFound == 1:
    if flagRepeatingElementsFound == True:
        print(f"\nOutput summary for longest common sub-sequences WITH repetition allowed:")
    else:
        print(f"\nOutput summary for longest common sub-sequences:")
    print(f"\nFound {len(finalLongestCommonSubSeqs)} common sub-sequence(s) for the input strings.")
    print(f"The longest common sub-sequence length = {len(finalLongestCommonSubSeqs[0])}")
    print(f"The sub-sequence(s):\n{finalLongestCommonSubSeqs}")
    
    if flagRepeatingElementsFound == True:
        print(f"\nOutput summary for longest common sub-sequences WITHOUT repetition allowed:")
        print(f"\nFound {len(finalLongestCommonSubSeqsWithoutRep)} common sub-sequence(s) for the input strings.")
        print(f"The longest common sub-sequence length = {len(finalLongestCommonSubSeqsWithoutRep[0])}")
        print(f"The sub-sequence(s):\n{finalLongestCommonSubSeqsWithoutRep}")
else:
    print("\nNO Common sub-sequence exists for the input strings.")
#exit(0)