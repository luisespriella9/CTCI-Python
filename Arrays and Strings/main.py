﻿def check(result, actualResult):
    #this is to check whether the answer is correct to the result we are expecting
    if result == actualResult:
        print("Correct")
    else:
        print("Issue Found")

# Problem 1.1
def isUnique(string):
    chars = [False] * 128
    for char in string:
        charNumber = ord(char)
        if chars[charNumber]:
            return False
        chars[charNumber] = True
    return True

# Problem 1.2
def checkPermutation(first, second):
    if (len(first) != len(second)):
        return False
    firstSet = [0]*128
    secondSet = [0]*128
    for i in range(len(first)):
        #fill both sets to count how many times each character appears for each word
        firstSet[ord(first[i])] += 1
        secondSet[ord(second[i])] += 1
    for i in range(128):
        #compare set results
        if firstSet[i] != secondSet[i]:
            return False
    return True

# Problem 1.3
def urlify(string, length):
    #replace all spaces with %20
    counter = 0
    resultingString = ""
    for char in string:
        if counter>=length:
            break
        if char == " ":
            resultingString += "%20"
        else:
            resultingString += char
        counter+=1
    return resultingString

# Problem 1.4
def palindromePermutation(string):
    string = string.lower()
    set = [0]*128
    for char in string:
        if (char.isalpha()):
            #only letters
            set[ord(char)]+=1
    counter = 0
    for charCount in set:
        if (counter>1):
            return False
        if (charCount%2 != 0):
            counter+=1
    return True

# Problem 1.5
def oneAway(first, second):
    if (first == second):
        #check if exact same word
        return True
    elif (len(first) == len(second)):
        if (len(first) == 1):
            #if both length of one and do not match given previous statement
            return False
        #check for replace character edit
        counter = 0
        for i in range(len(first)):
            if (counter > 1 ):
                return False
            if (first[i] != second[i]):
                counter += 1
        return True
    else:
        #check for inserting or removing character. Get biggest string and find if any subset matches other string
        if (len(first) > len(second)):
            bigger = first
            smaller = second
        else:
            bigger = second
            smaller = first
        for i in range(len(bigger)):
            subset = bigger[:i]+bigger[i+1:]
            if (subset == smaller):
                return True
        #as long as subset doesnt match smaller string
        return False

# Problem 1.6
def stringCompression(string):
    if (string == ""):
        return ""
    #latest char be the first char in the string
    latestChar = string[0]
    charAppearances = 0
    compressedString = ""
    for char in string:
        if not char.isalpha():
            continue
        if (latestChar == char):
            charAppearances += 1
        else:
            compressedString += str(latestChar) + str(charAppearances)
            charAppearances = 1
            latestChar = char
    compressedString += str(latestChar) + str(charAppearances)
    #check if compressed String is actually smaller, if not return original string
    if (len(compressedString) < len(string)):
        return compressedString
    else:
        return string

# Problem 1.7
def rotateMatrix():
    return ""

# Problem 1.8
def zeroMatrix():
    return ""

# Problem 1.9
def stringRotation(first, second):
    return ""

if __name__ == "__main__":
    print("Test isUnique")
    check(isUnique("hello"), False)
    check(isUnique("why"), True)

    print("Test checkPermutation")
    check(checkPermutation("aba", "baa"), True)
    check(checkPermutation("abb", "aba"), False)

    print("Test URLify")
    check(urlify("Mr John Smith     ", 13), "Mr%20John%20Smith")

    print("Test Palindrome Permutation")
    check(palindromePermutation("Tact Coa"), True)

    print("Test One Away")
    check(oneAway("pale", "ple"), True)
    check(oneAway("pales", "pale"), True)
    check(oneAway("pale", "bale"), True)
    check(oneAway("pale", "bake"), False)

    print("Test String Compression")
    check(stringCompression("aabcccccaaa"), "a2b1c5a3")
    check(stringCompression("aabccccca"), "a2b1c5a1")
    check(stringCompression("a"), "a")

    print("Test Rotate Matrix")

    print("Test Zero Matrix")

    print("Test String Rotation")
    check(stringRotation("waterbottle","erbottlewat"), True)