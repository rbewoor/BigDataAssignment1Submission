"""
# -*- coding: utf-8 -*-
# 28 April 2019
# Big Data Programming - Assignment 1 - Problem 2: Match a string S1 with a pattern defined by string S2 and indicate if S1 matches or not
#   Rules:
#       For string 1: the string to be matched with the pattern
#               only lowercase alphabets allowed, no special characters and any leading/ trailing/ interspersed spaces will be discarded
#       For string 2: the pattern
#               only lowercase alphabets allowed, no special characters and any leading/ trailing/ interspersed spaces will be discarded
#   Example 1:
#       Inputs:                 String1 = "aba"             String2 = "*ab"
#       Expected output:        False
#   Example 2:
#       Inputs:                 String1 = "aa"              String2 = "a*"
#       Expected output:        True
#   Example 3:
#       Inputs:                 String1 = "ab"              String2 = ".*"
#       Expected output:        True
#   Example 4:
#       Inputs:                 String1 = "ab"              String2 = "."
#       Expected output:        False
#   Example 5:
#       Inputs:                 String1 = "aab"             String2 = "c*a*b"
#       Expected output:        True
#   Example 6:
#       Inputs:                 String1 = "aaa"             String2 = "a*"
#       Expected output:        True
#
"""
#
##
####            function definitions start
##
#
def f1_perform_sanity_checks_on_input_strings(inS1, inS2):
    """ Performs basic sanity checks on the two input strings to verify that they meet input rules and convert the strings to
        a format that is suitable for processing further.
        Returns two cleaned version for String1 and String2 and error codes for overall, string1 and string2
    Input parameters:
        inS1:       the first input string that is to be matched
        inS2:       the second input string that is the pattern
    Output parameters:
        outS1:      the santized string 1
        outS2:      the santized string 2
        overallRC:  overall return code
        str1RC:     return code for String 1
        str2RC:     return code for String 2
        str1RCMsg   error message for String 1
        str2RCMsg   error message for String 2
        Return code:
                -----------------------------------------------------------
                Value       Meaning
                -----------------------------------------------------------
                ---  OVERALL RETURN CODE :: 100 series of error codes  ---
                0           All ok with both input strings
                1           Problem with String 1 only
                2           Problem with String 2 only
                3           Problem with BOTH strings
                -----------------------------------------------------------
                ---  STRING 1 ERROR CODES :: 100 series of error codes  ---
                0           String-1 All ok.
                101         <<<<<Not used>>>>>
                102         String-1 Empty input detected after basic cleanup.
                -----------------------------------------------------------
                ---  STRING 2 ERROR CODES :: 200 series of error codes  ---
                0           String-2 All ok
                201         String-2 Invalid input:: only a-z (lower or upper case with spaces), DOT and STAR operators allowed.
                202         String-2 Empty input detected after basic cleanup.
                -----------------------------------------------------------
    """
    overallRC = 3
    str1RC = 199    # initialised to someting random
    str2RC = 299    # initialised to someting random
    str1RCMsg = str2RCMsg = "String evaluation pending"
    
    outS1 = inS1
    outS2 = inS2
    # remove leading, trailing and midway whitespaces
    outS1 = outS1.lower()
    outS2 = outS2.lower()
    outS1 = outS1.strip()
    outS2 = outS2.strip()
    outS1 = "".join(outS1.split())
    outS2 = "".join(outS2.split())

    # checks for String 1 and set the RC and Message for String 1
    if len(outS1) == 0:
        str1RC = 102
        str1RCMsg = "String-1 Empty input detected after basic cleanup."
    else:
        str1RC = 0
        str1RCMsg = "String-1 All ok."
    
    # checks for String 2 and set the RC and Message for String 2, and the overall RC code
    if len(outS2) == 0:
        str2RC = 202
        str2RCMsg = "String-2 Empty input detected after basic cleanup."
        if str1RC == 0:
            overallRC = 2
        else:
            overallRC = 3
        return (outS1, outS2, overallRC, str1RC, str2RC, str1RCMsg, str2RCMsg)
    else:
        # first check if after disregarding all DOT and STAR operators, the remaining string is still alphabetic if it is not blank
        outS2temp = outS2.replace("*","")
        outS2temp = outS2temp.replace(".","")
        if outS2temp.isalpha() == True:     # stripping off all DOT and STAR from S2 should retain only alphabets
            str2RC = 0
            str2RCMsg = "String-2 All ok."
            if str1RC == 0:
                overallRC = 0
            else:
                overallRC = 1
            return (outS1, outS2, overallRC, str1RC, str2RC, str1RCMsg, str2RCMsg)
        elif len(outS2) == ( outS2.count("*") + outS2.count(".") ):    # if its not alphabetic in above check, S2 must be only STAR and DOTS
            str2RC = 0
            str2RCMsg = "String-2 All ok."
            if str1RC == 0:
                overallRC = 0
            else:
                overallRC = 1
            return (outS1, outS2, overallRC, str1RC, str2RC, str1RCMsg, str2RCMsg)
        else:
            str2RC = 201
            str2RCMsg = "String-2 Invalid input:: only a-z (lower or upper case with spaces), DOT and STAR operators allowed."
            if str1RC == 0:
                overallRC = 2
            else:
                overallRC = 3
            return (outS1, outS2, overallRC, str1RC, str2RC, str1RCMsg, str2RCMsg)
##########
def f2_trivial_and_boundary_condition_checks(workS1, workS2):
    """ Performs basic boundary checks and return output for TRIVIAL cases which should hold due to basic cleanup
        and collapse of repeating STAR operator.
        Returns processing completion flag and Boolean output
    Input parameters:
        workS1:       the string to be matched
        workS2:       the pattern string
    Output parameters:
        retCode:    return code indicating the trivial condition (defaults to 0, if actual condition found then 2 or 3 or 4)
        outBoolean: returns as True or False to indicate if S1 matched S2 or not
    """
    # logic for some boundary condition TRIVIAL cases where output can be determined easily
    # Return Code) -- condition description
    # 1) -- S1 MUST be alphabetic values -- already checked earlier in logic and no need to check here anymore
    # 2) -- S2 starting with a STAR operator means no match is possible irrespective of S1. Output ALWAYS = False
    # 3) -- REDUNDANT CONDITION - TOO LITTLE TIME TO CHANGE CODE NOW: If S2 begins with ".*" , irrespective of S1 Output ALWAYS = True
    # 4) -- If S2 has no STAR operator at all, then number of alphabets and DOTs present in S2 MUST BE AT LEAST = characters in S1
    #
    retCode = 0
    outBoolean = False
    if workS2.startswith("*") == True:    # check for condition 2
        outBoolean = False
        retCode = 2
        #print(f"Trivial condition 2 detected:: String 2 starts with STAR operator")
        return(retCode, outBoolean)
    # check for condition 3 - REDUNDANT BUT OUT OF TIME TO CHANGE
    # elif workS2.startswith(".*"):                    # check for condition 3 - REDUNDANT BUT OUT OF TIME TO CHANGE
    #     outBoolean = True
    #     retCode = 3
    #     print(f"Trivial condition 3 detected:: String 2 starts with '.*' so any non zero length S1 MUST match")
    #     return(retCode, outBoolean)
    elif workS2.count("*") == 0:   # if there are no STAR operators in S2  then check for trivial condition 4
        if len(workS1) > len(workS2):
            outBoolean = False
            retCode = 4
            #print(f"Trivial condition 4 detected:: String 2 has no STAR operator and is too short to bother matching with S1 input")
            return(retCode, outBoolean)
    return(retCode, outBoolean)
#
##########
def f3_display_final_output(finalOuputBoolean, origIpS1, origIpS2, workS1, workS2):
    """ Performs display to console of the final output values and exits the program to OS.
    Input parameters:
        finalOuputBoolean:      the output Boolean value to show as answer
        origIpS1:               the string-1 entered by user that was to be matched
        origIpS2:               the string-2 entered by user that defines the pattern
        workS1:                 the working string-1 created after basic checks and that was used for the main logic
        workS2:                 the working string-2 created after basic checks and that was used for the main logic
    Output parameters:
        None
    """
    # final output display setup and printing to console
    if finalOuputBoolean == False:
        finalOutputMessage = "S1 does NOT match with S2"
    else:
        finalOutputMessage = "S1 MATCHES with S2"
    print(f"\n\nFINAL OUTPUT STAGE...")
    print(f"Your input for String 1:\n{origIpS1}\nYour input for String 2:\n{origIpS2}")
    print(f"Working String 1:\n{workS1}\nWorking String 2:\n{workS2}")
    print(f"\nfinalOuputBoolean= {finalOuputBoolean}\nfinalOutputMessage= {finalOutputMessage}")
    return()
#
##########
def f5_detect_complex_condition(s2, s2Idx):
    """ Performs check to identify which condition is met by S2 and returns the condition number
    Input parameters:
        s1:       the string to be matched
        s2Idx:    the starting position to begin the condition check from
    Output parameters:
        condition number:   integer (defaults to 0 if there is no matching condition found and that is a problem logic wise)
    """
    # Elemental conditions and description as you move from Left to Right parsing String-2. The @ represents any alphabet below and | is to
    #       distinguish one logical block from the next 
    # 1) "@|@whatever" or  "@|.whatever"
    #       expecting match of the @ of S2 against the same alphabet in S1
    # 2) "@*|whatever"
    #       expecting match of @ of S2 against same alphabet in S1. Then any succeeding alphabets in S1 that are repeating.
    # 3) ".|@whatever" or  ".|.whatever"
    #       expecting match of the DOT of S2 against any alphabet in S1
    # 4) ".*|whatever or end of string"
    #       expecting match of the DOT in S2 against any alphabet in S1. Output decided now, without bothering to check anything more in S1.
    #       CONDITION 4 IS NOW REDUNDANT AS   DOT-STAR   logic is done as a basic trivial check and will never be encountered here
    # 5) "@|nothing more as string ends"
    #       expecting match of @ of S2 against same alphabet in S1. Then output determined by checking if S1 is also over or not.
    # 6) ".|nothing more as string ends"
    #       expecting match of the DOT in S2 against any alphabet in S1. Then output determined by checkign if S1 is also over or not.
    # 7) "|nothing more as string ends"
    #       Nothing to compare as S2 is already ended.
    # N.B. THERE SHOULD BE NO WAY THAT WE GET A  STAR  AT THE INDEX POSITION FOR EVALUATION
    #
    condNo = 0   # initialised to zero which indicates a problem on return
    if s2Idx >= len(s2):
        condNo = 7
    elif s2Idx == len(s2) - 1:
        # this is the last character of S2
        if s2[s2Idx].isalpha() :     # some @ and S2 ends
            condNo = 5
        elif s2[s2Idx] == ".":       # a . and S2 ends
            condNo = 6
    else:
        # we are not at the last character in S2 still
        if s2[s2Idx] == "." :
            condNo = 3          # no need to both checking whether next character is a *. It has to be either an alphabet or another DOT
            #if s2[s2Idx + 1] == "*" :
            #    condNo = 4                      # its a condition of  ".*" 
            #else:
            #    condNo = 3                      # its either a condition of   "..   or   ".@"
        else:
            # the s2Idx positon is an alphabet
            if s2[s2Idx + 1] == "*" :
                condNo = 2
            else:
                condNo = 1
    return(condNo)
#
##########
def f4_complex_checks(workS1, f4workS2):
    """ Performs the non-trivial condition checks to find a match.
        Returns processing completion flag and Boolean output
    Input parameters:
        workS1:       the string to be matched
        workS2:       the pattern string
    Output parameters:
        flagDone:   returns as True if output was identified, otherwise False
        outBoolean: returns as True or False to indicate if S1 matched S2 or not
    """
    flagDone = outBoolean = False   # initialised both to be False.
    s1Idx = f4s2Idx = f5condNo = 0
    while s1Idx < len(workS1):
        f5condNo = f5_detect_complex_condition(f4workS2, f4s2Idx)
        if f5condNo == 7:
            if s1Idx < len(workS1):
                outBoolean = False  # there are still characters in S1 but S2 is finished, so S1 cannot be a substring
            else:
                outBoolean = True   # S1 is also over at same time as S2 is finished
            flagDone = True
            break
        elif f5condNo == 1:           # @
            if f4workS2[f4s2Idx] != workS1[s1Idx]:
                flagDone = True
                outBoolean = False
                break
            s1Idx = s1Idx + 1
            f4s2Idx = f4s2Idx + 1
        elif f5condNo == 2:       # @*
            if f4workS2[f4s2Idx] != workS1[s1Idx]:
                flagDone = True
                outBoolean = False
                break
            f4s2Idx = f4s2Idx + 2
            while workS1[s1Idx] == f4workS2[f4s2Idx-2]:
                s1Idx = s1Idx + 1
                if s1Idx >= len(workS1):
                    break
        elif f5condNo == 3:       # .
            s1Idx = s1Idx + 1
            f4s2Idx = f4s2Idx + 1
        elif f5condNo == 4:       # .*
            break    # was being used earlier but found a better approach that makes this condition redundant
            # outBoolean = True
            # flagDone = True
            # break
        elif f5condNo == 5:       # @ at the end of S2 string
            #   Are S1 and S2 value equal?              Is S1 string ended                  Final output
            #           No                                Does not matter                       False
            #           Yes                               Yes                                   True
            #           Yes                               No                                    False
            #
            s1Idx = s1Idx + 1
            f4s2Idx = f4s2Idx + 1
            if f4workS2[f4s2Idx - 1] != workS1[s1Idx - 1]:
                outBoolean = False
            else:
                if s1Idx >= len(workS1):
                    outBoolean = True
                else:
                    outBoolean = False
            break
        elif f5condNo == 6:       # . at the end of S2 string
            s1Idx = s1Idx + 1
            f4s2Idx = f4s2Idx + 1
            if s1Idx < len(workS1):  # as S2 has ended, check if S1 also ended. If yes thats fine, but if S1 still has stuff then output shoudl be false.
                outBoolean = False
            else:
                outBoolean = True
            flagDone = True
            break
        else:
            print(f"PROBLEM::: func5 condition code was {f5condNo}.\nUnable to determine correct output")
            exit(0)
    if s1Idx >= len(workS1):    #
        flagDone = True
        if f5condNo != 5 and f5condNo != 6:
            outBoolean = True

    return(flagDone, outBoolean)
#
##
####            function definitions ended
##
#
##
####            MAIN PROGRAM STARTS
##
#
# two hard coded strings as input
# origIpS1 = "dca bFa1diMAC v bACSa a"
# origIpS2 = "  arBAF t1*vdc.bq aa"
# take inputs from console, perfrom basic sanity checks and ask user to re-input strings till they are both correctly provided
overallRC = 3
while overallRC != 0:
    print("\n\n")
    if overallRC == 3 or overallRC == 1:
        origIpS1 = input("Please enter string 1, case conversion to lower and whitespace removal will be automatic:\n")
    if overallRC == 3 or overallRC == 2:
        origIpS2 = input("Please enter string 2, only a-z and STAR and DOT allowed, case conversion to lower and whitespace removal will be automatic:\n")
    str1RCMsg = str2RCMsg = "Default Message -- means nothing"
    overallRC = 3   # defaulting to assume error on both strings
    str1RC = 199    # initialised to someting random
    str2RC = 299    # initialised to someting random
    workS1, workS2, overallRC, str1RC, str2RC, str1RCMsg, str2RCMsg = f1_perform_sanity_checks_on_input_strings(origIpS1, origIpS2)
    
    if overallRC == 0:
        print("\n\nBoth input strings accepted for further processing:")
        #print(f"For String 1:\nReturn Code str1RC=\n{str1RC}\nMessage str1RCMsg=\n{str1RCMsg}")
        #print(f"For String 2:\nReturn Code str1RC=\n{str2RC}\nMessage str2RCMsg=\n{str2RCMsg}")
        print(f"\nYour input for String 1:\n{origIpS1}\nYour input for String 2:\n{origIpS2}")
        print(f"Cleaned up String 1:\n{workS1}\nCleaned up String 2:\n{workS2}")
    elif overallRC == 3:
        print(f"\n\nErrors detected for BOTH strings during basic clean up process")
        print(f"For String 1:\nReturn Code str1RC=\n{str1RC}\nMessage str1RCMsg=\n{str1RCMsg}")
        print(f"For String 2:\nReturn Code str1RC=\n{str2RC}\nMessage str2RCMsg=\n{str2RCMsg}")
        print(f"Your input for String 1:\n{origIpS1}\nYour input for String 2:\n{origIpS1}")
        print(f"You need to reenter both strings....")
    elif overallRC == 1:
        print(f"\n\nError detected for String 1 ONLY during basic clean up process. String 2 is accepted for processing.")
        print(f"For String 1:\nReturn Code str1RC=\n{str1RC}\nMessage str21CMsg=\n{str1RCMsg}")
        print(f"Your input for String 1:\n{origIpS1}")
        print(f"You need to reenter only String 1....")
    else:                                                                   # corresponds to overallRC = 2
        print(f"\n\nError detected for String 2 ONLY during basic clean up process.  String 1 is accepted for processing.")
        print(f"For String 2:\nReturn Code str2RC=\n{str2RC}\nMessage str2RCMsg=\n{str2RCMsg}")
        print(f"Your input for String 2:\n{origIpS2}")
        print(f"You need to reenter only String 2....")
#
##                      main logic for pattern matching beings
#   S1 is the string to be matched        S2 is the pattern string        Does S1 match S2?
#   Another way to ask this is: Is S1 string a substring of any elements of the set of strings that are defined by the pattern S2?
#       S2 could be a set of infinite possible strings too.
#
#   parse S2 and collapse any repeating STAR operators into just one STAR.
#       E.g.        "..abc****fb***nm*****"        is converted to    "..abc*fb*nm*"
tempWorkS2 = prevChar = ""          
for currentChar in workS2:
    if currentChar == "*" and prevChar == "*":
        prevChar = currentChar
        continue
    else:
        tempWorkS2 = tempWorkS2 + currentChar
        prevChar = currentChar
if workS2 != tempWorkS2:
    print(f"\nPattern String 2 changed:: all repeating STAR operators collapsed to one STAR as the change has no effect on pattern set")
    print(f"Pattern String 2 after change =\n{tempWorkS2}\n")
    workS2 = tempWorkS2
#
#   ended repeating STAR collapse logic
#
#   parse S2 and collapse any consecutive  DOT-STAR   to single DOT-STAR
#       E.g.        ".*ac.*.*asdf.*.*.*.**.*.*.*fr...f.*.*.*"        is converted to    ".*ac.*asdf.**.*fr...f.*"
tempWorkS2 = ""
idx = countDotStarInWorkS2 = prevDsIdx = 0
countDotStarInWorkS2 = workS2.count(".*")
if countDotStarInWorkS2 > 1:    # multiple DOT-STAR present, proceed with collapsing check
    for i in range(countDotStarInWorkS2):
        dsIdx = workS2.find(".*", idx)
        if i == 0:
            tempWorkS2 = tempWorkS2 + workS2[ 0 : dsIdx + 2 ] # found and copied from beginning till end of the first DOT-STAR
        else:
            if (dsIdx - prevDsIdx) > 2:    # successive DOT-STAR will have difference of 2, and so should not be copied
                tempWorkS2 = tempWorkS2 + workS2[ prevDsIdx + 2 : dsIdx + 2 ]
        idx = dsIdx + 2
        prevDsIdx = dsIdx
    if len(workS2) > (dsIdx + 2):  # true if more characters present after the last ".*"
        tempWorkS2 = tempWorkS2 + workS2[ dsIdx + 2 : ]
else:
    tempWorkS2 = workS2
if workS2 != tempWorkS2:
    print(f"\nPattern String 2 changed:: all successive DOT-STAR combos collapsed to one DOT-STAR")
    print(f"Pattern String 2 after change =\n{tempWorkS2}\n")
workS2 = tempWorkS2
# 
#   ended DOT-STAR collapse logic
flagFinalOpBool = False
# MOST TRIVIAL contional checks
# if the S1 string itself is non alphabetic then trivial case of ouputting False
if workS1.isalpha() == False:           # check for trivial condition 1
    flagFinalOpBool = False
    #print(f"\nBasic Trivial condition detected:: String 1 is not alphabetic")
    f3_display_final_output(flagFinalOpBool, origIpS1, origIpS2, workS1, workS2)
    exit(0)
# if the S2 string has a  DOT-STAR  anywhere in it, then if the S1 string is not NULL-String and is alphabetic, then o/p must be TRUE
if workS2.find(".*") != -1  and   workS1 != "":           # found a DOT-STAR
    flagFinalOpBool = True
    #print(f"\nBasic Trivial condition detected:: String 2 has DOT-STAR present")
    f3_display_final_output(flagFinalOpBool, origIpS1, origIpS2, workS1, workS2)
    exit(0)
#
for startIdxForS2 in range(len(workS2)):
    flagOuputBooleanTrivial = False
    #print(f"\nStaring loop number:\n{startIdxForS2+1}\nand workS2 passed as:\n{workS2[startIdxForS2:]}")
    f2retCode = 0
    f2retCode, flagOuputBooleanTrivial = f2_trivial_and_boundary_condition_checks( workS1, workS2[startIdxForS2:] )
    if f2retCode != 0:  # some trivial condition detected
        if f2retCode == 2:                          
            continue                                # S2 started with * for this loop, continue to next round of loop
        else:
            if f2retCode == 4:                      
                flagFinalOpBool = False             # S2 len(S2) too short compared to len(S1)
            else:
                flagFinalOpBool = True              # f2retCode=3 => S2 started with .*
            break                                   # break in both cases of retCode of 3 and 4
    else:                                           # no trivial condition detected
        flagProcessingDoneComplex = flagOuputBooleanComplex = False
        #print(f"NO TRIVIAL CASES DETECTED for loop number {startIdxForS2+1}.\nProceeding for complex checks...")
        flagProcessingDoneComplex, flagOuputBooleanComplex = f4_complex_checks( workS1, workS2[startIdxForS2:] )
        if flagProcessingDoneComplex == True:
            if flagOuputBooleanComplex == True:
                flagFinalOpBool = True
                break
        else:
            print(f"PROBLEM at end of loop number {startIdxForS2+1}...")
            print(f"Unable to determine output. Exiting program....")
            exit(0)
#
f3_display_final_output(flagFinalOpBool, origIpS1, origIpS2, workS1, workS2)
exit(0)