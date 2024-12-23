"""
    written by bcl0c, whose code will make you bleed through your pores.

    
    basically the same as mergesort with a slightly modified merge. Ultrafun!
"""

def mergeCount(partA: list[int], partB: list[int], earlierSumCount): #works for even stupid ass big numbers somewhat fast.
    # partA -> the left partition of what we're merging
    # partB -> the right partition of what we're merging
    # earlierSumCount -> sum of earlier inversions, we'll augment this sucker here.

    #starts the same as normal Alpha merge, create aux and go on.
    res = []
    sum = earlierSumCount
    while len(partA) * len(partB) > 0: #if any hits 0, multiplication goes to 0, loop stops.
        if partA[0] < partB[0]: #partB always greater or equal in length
            res.append(partA.pop(0))
            continue
        #this is the major modification here, besides the return.
        sum += len(partA)
        res.append(partB.pop(0))
        #debug. I want to see these mikefoxtrots get popped
        """ 
        print("!DEBUG! -----------")
        print(partA)
        print(partB)
        print(res)
        print("<------------------>") 
         """
    #copy rest of stragglers and foxtroters.
    #at least one of these fuckers won't activate, so all's fine and stuff.
    while len(partA) > 0: 
        res.append(partA.pop(0))
    while len(partB) > 0: 
        res.append(partB.pop(0))
    """ 
    print("!DEBUG! Done :> -----------")
    print(res)
    print("<------------------>")  
    """
    return res, sum

def invertionCount(this: list[int], count: int = 0):
    #ah yeah, this returns the sorted list AND the count.
    a = len(this)
    a = a//2
    #if len == 1
    if len(this) == 1:
        #basecase this mf
        #return what was passed,
        #and invcount = 0, as it was completely and utterly
        #!sorted!
        return this, 0
    
    #else we actually do something
    partA, countA = invertionCount(this[:a], count)
    partB, countB = invertionCount(this[a:], count)

    merged, sum = mergeCount(partA, partB, countA + countB)
    return merged, sum

def mergeCounttester() -> None:
    # as finding if we've got the correct amount of counts
    # for two sorted arrays would imply, much unfortunately,
    # we already had this algorithm tested and running correctly, 
    # i'll have to hardcode the expected amount instead of doing an actual 
    # pretty tested function and stuff, which is not very great.
    print("starting minor testing routine mergeCounttester!")

    partA = [3, 7, 10, 14, 18, 19]
    partB = [2, 11, 16, 17, 23, 25]

    expected = 13 #this is the expected thing. 
    print("partA ->", partA)
    print("partB ->", partB)
    merged, sum = mergeCount(partA, partB, 0)
    print("-----------------")
    print("merged ->", merged )

    if sum == expected:
        print("TEST SUCCESFUL")
    else:
        print("TEST FAILED")

if __name__ == "__main__":
    mergeCounttester()
