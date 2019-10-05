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

#problem 10.2
def searchSorted(array, target):
    return searchSortedIter(array, target, 0, len(array)-1)

def searchSortedIter(array, target, leftIndex, rightIndex):
    if (rightIndex-leftIndex < 0): 
        #if length == 0
        return None
    midIndex = int((leftIndex+rightIndex)/2)
    midVal = array[midIndex]
    if (midVal == target):
        return midIndex
    lastVal = array[rightIndex]
    if (lastVal == target):
        return rightIndex
    if (midVal < lastVal):
        if ((target > midVal) and (target < lastVal)):
            #in right side, seach in sorted array
            return binarySearch(array, target, midIndex, rightIndex)
        else:
            return searchSortedIter(array, target, leftIndex, midIndex-1)
    else:
        if ((target < midVal) and (target > lastVal)):
            #in left side, search in sorted array
            return binarySearch(array, target, leftIndex, midIndex)
        else:
            return searchSortedIter(array, target, leftIndex+1, rightIndex)

#helpful functions
def binarySearch(array, target):
    leftIndex = 0
    rightIndex = len(array)-1
    while (leftIndex <= rightIndex):
        midIndex = int((leftIndex+rightIndex)/2)
        midValue = array[midIndex]
        if (midValue == target):
            return midIndex
        elif (target < midValue):
            rightIndex = midIndex - 1
        else:
            leftIndex = midIndex + 1
    return None

#override
def binarySearch(array, target, leftIndex, rightIndex):
    while (leftIndex <= rightIndex):
        midIndex = int((leftIndex+rightIndex)/2)
        midValue = array[midIndex]
        if (midValue == target):
            return midIndex
        elif (target < midValue):
            rightIndex = midIndex - 1
        else:
            leftIndex = midIndex + 1
    return None

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

    print("---------------------------------")
    print("Test Search in Rotated Array")
    testArray = [15, 16, 19, 20, 25, 1 , 3, 4, 5, 7, 10, 14]
    testArray2 = [15, 16, 19, 20, 25, 27 , 3, 4, 5, 7, 10, 14]
    testArray3 = [1, 2, 5]
    testArray4 = [1, 2]
    testArray5 = [1]
    check(searchSorted(testArray, 15), 0)
    check(searchSorted(testArray, 16), 1)
    check(searchSorted(testArray, 25), 4)
    check(searchSorted(testArray, 1), 5)
    check(searchSorted(testArray, 5), 8)
    check(searchSorted(testArray, 14), 11)
    check(searchSorted(testArray2, 15), 0)
    check(searchSorted(testArray2, 16), 1)
    check(searchSorted(testArray2, 25), 4)
    check(searchSorted(testArray2, 3), 6)
    check(searchSorted(testArray2, 5), 8)
    check(searchSorted(testArray2, 14), 11)
    check(searchSorted(testArray3, 1), 0)
    check(searchSorted(testArray3, 2), 1)
    check(searchSorted(testArray3, 5), 2)
    check(searchSorted(testArray4, 1), 0)
    check(searchSorted(testArray4, 2), 1)
    check(searchSorted(testArray5, 1), 0)