def check(result, actualResult):
    #this is to check whether the answer is correct to the result we are expecting
    if result == actualResult:
        print("Correct")
    else:
        print("Issue Found")

def mergeSort(list):
    if (len(list) == 1):
        return [list]
    mid = int((len(list))/2)
    return merge(mergeSort(list[:mid]), mergeSort(list[mid+1:]))

def merge(leftList, rightList):
    print("left list: ", leftList)
    print("right List: ", rightList)
    leftPointer = 0
    rightPointer = 0
    while (leftPointer < len(leftList)):
        if (rightList[rightPointer] < leftList[leftPointer]):
            leftList.insert(leftPointer, rightList[rightPointer])
            rightPointer += 1
        if (leftPointer == (len(leftList)-1)):
            break
        leftPointer +=1
    return leftList

if __name__ == "__main__":
    print("Test Mergesort")
    unsorted = [1, 4, 5, 2, 8, 9]
    sorted = [1, 2, 4, 5, 8, 9]
    check(mergeSort(unsorted), sorted)
    