def check(result, actualResult):
    #this is to check whether the answer is correct to the result we are expecting
    if result == actualResult:
        print("Correct")
    else:
        print("Issue Found")

#problem 10.1
def sortedMerge(arrayA, arrayB):
    if (len(arrayB) == 0):
        return arrayA
    pointerA = 0
    pointerB = 0
    while (pointerB < len(arrayB)):
        if (pointerA >= len(arrayA)):
            #just add the rest of B
            arrayA.insert(pointerA, arrayB[pointerB])
            pointerB += 1
            continue
        if (arrayA[pointerA] >= arrayB[pointerB]):
            arrayA.insert(pointerA, arrayB[pointerB])
            pointerB += 1
        pointerA += 1
    return arrayA

#problem 10.2
def groupAnagrams(list):
    anagramDict = {}
    sortedChecker = []
    for item in list:
        s_item = ""
        for c in sorted(item):
            s_item += c
        if (s_item in anagramDict):
            anagramDict[s_item].append(item)
        else:
            anagramDict[s_item] = [item]
    output = []
    for anagramGroup in anagramDict.values():
        output.append(anagramGroup)
    return output

if __name__ == "__main__":
    print("Test Sorted Merge")
    arrayA = [1, 5, 7, 9, 10, 12]
    arrayB = [2, 6, 8]
    check(sortedMerge(arrayA, arrayB), [1, 2, 5, 6, 7, 8, 9, 10, 12]) #start with A
    arrayA = [1, 5, 7, 9, 10, 12]
    arrayB = [0, 2, 6, 8]
    check(sortedMerge(arrayA, arrayB), [0, 1, 2, 5, 6, 7, 8, 9, 10, 12]) #start with B
    arrayA = []
    arrayB = [6, 8]
    check(sortedMerge(arrayA, arrayB), [6, 8]) #A is empty -> "return B" however function should merge B into A
    arrayA = [1]
    arrayB = []
    check(sortedMerge(arrayA, arrayB), [1]) #B is empty -> return A
    arrayA = []
    arrayB = []
    check(sortedMerge(arrayA, arrayB), []) #both are empty -> return either

    print("---------------------------------")
    print("Test Group Anagrams")
    list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    check(groupAnagrams(list), [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])