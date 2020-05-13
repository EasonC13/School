print("'\033[95m" +"PriceTable 從零開始算，為了演算法方便\n")
PriceTable = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def CutRod(PriceTable, n, r = None, s = None):
    print("now running %d"%n, end = "")
    if n == 0 or n == 1:
        print("  return %d"%n)
        return n, r, s
    
    if r == None:
        r = createR(n)
    if s == None:
        s = createS(n)
        
    if r[n] != 0:
        print(" return %d for pervious example."%r[n])
        return r[n], r, s
    
    print("a Not found, start calculate:")
    currentMax = float('-inf')
    for i in range(0,n):
        print("split to %d, %d"%(i, n-i))
        cut = CutRod(PriceTable, i, r, s)[0] + PriceTable[n-i]
        print("This type of split (%d, %d) is = %d\n"%(i, n-i, cut))
        if currentMax < cut:
            currentMax = cut
            s[n] = i
    print("The max splite of %d is %d\n"%(n, currentMax))
    r[n] = currentMax
    return currentMax, r, s
        
        
        
def createR(n):
    return [0] * (n+1)
def createS(n):
    return [0] * (n+1)

CutRod(PriceTable, 10)