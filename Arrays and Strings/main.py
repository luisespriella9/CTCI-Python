def check(result, actualResult):
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
        firstSet[ord(first[i])] += 1
        secondSet[ord(second[i])] += 1
    for i in range(128):
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
            #only count letters
            set[ord(char)]+=1
    counter = 0
    for charCount in set:
        if (counter>1):
            return False
        if (charCount%2 != 0):
            counter+=1
    return True

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