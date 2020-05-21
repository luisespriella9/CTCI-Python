def check(result, actualResult):
    #this is to check whether the answer is correct to the result we are expecting
    if result == actualResult:
        print("Correct")
    else:
        print("Issue Found")

class fibonacci:
    def __init__(self):
        self.mem = [None]*500 #size that we can save unto

    def getFibonacci(self, n):
        if (self.mem[n] != None):
            return self.mem[n]
        else:
            return self.compute(n)

    def compute(self, n):
        if ((n==0) or (n==1)):
            return n
        return getFibonacci(n-1)+getFibonacci(n-2)

if __name__ == "__main__":
    print("Fibonacci example using DP")