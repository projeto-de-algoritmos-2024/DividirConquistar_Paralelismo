"""
Written by bcl0c.  violence :>

Warning ZERO: this guy starts taking a long Alpha time to sort numbers upward of a million 
    entries. Be very aware of that :>>>.

Warning 1: This code uses the patented (not really) locvst's (no proof
of invention) NATO Styled Secure Cursing Commentary system.
    If for whatever reason you see a NATO Phonetic Alphabet just 
    there on some random Alpha comment, be sure it was a curse
    and it got secured (censored). 
    Major changes are papa -> phantom.

Warning 2: JulietCharlieIndiaIndiaHotelNovember

This code is done so we may test its performance against other
contenders in this great paralelization race.
Alright, initial stuff outta the way, here comes the useful stuff:

Merge:
    Gets two ordered vectors. 
    Spits out a nice and ordered vector.

Partition: 
    Gets a vector, breaks it apart by two, usually. 
    If odd length, greater part goes left.

    If parts greater than two, will return a list of 
    indexes instead, which is, of course, undefined behaviour.

MergeSort:
    Gets an array of items
    Sorts it by subdividing it then
    merging the parts.

General commentary:
    comment 1 (221220242014):
        We'll be trying to always put the greater length 
        on the left when doing half partitions (n=2).
        n > 2 types are quite exquisite, so i don't really
        plan on implementing such a merge, since it would 
        involve working with n > 2 indexes of a merge,
        which ain't very great...

    comment 2 (221220242029):
        foxtrot putting the smaller length on the left
        side, integer division will not round. If it got the ceiling,
        then it would. But i ain't putting an if inside the 
        code because i want to force the smaller length 
        to the left. 
        That would be rat behaviour. 

"""


def merge(partA: list[int], partB: list[int]) -> list[int]: #works for even stupid ass big numbers somewhat fast.
    res = []
    while len(partA) * len(partB) > 0: #if any hits 0, multiplication goes to 0.
        if partA[0] < partB[0]: #partB always greater or equal in length
            res.append(partA.pop(0))
            continue
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
    return res

def mergeSort(this: list[int]):
    #if len == 1, then
    if len(this) == 1:
        #already sorted, return this mf
        return this
    #else, we run the actual algorithm
    a = len(this)
    a = a//2 

    #we ain't doing sierra else merge whatever crawls backup
    #then, let's see what crawls.
    partA = mergeSort(this[:a])
    partB = mergeSort(this[a:])
    
    merged = merge(partA, partB)

    return merged

def checkIfSorted(somelist):
    
    for i in range(len(somelist) - 1):
        if somelist[i] > somelist[i+1]:
            return False
    else:
        return True

""" #this is theMerge test routine. It tests merging two sorted arrays.
if __name__ == "__main__":

    
    #verdict -> merge working!
    
    print("STARTING thegreat TEST ROUTINE!")
    import random
    try:
        a = int(input("Give n: "))
    except:
        print("not int. quiting")
        quit()

    b = input("Give seed: ")
    print("generating lists")
    random.seed(b)
    list1 = []
    list2 = []
    for _ in range(a):
        list1.append(random.randint(a = 0, b = 1000))
        list2.append(random.randint(a = 0, b = 1000))

    
    list1.sort()
    list2.sort()

    print(list1)
    print(list2)
    z = merge(list1, list2)
    print(z)
 """

    

#this is TheGreat test routine. It actually tests the mergeSort.
if __name__ == "__main__":
    print("STARTING thegreat TEST ROUTINE!")
    import random
    try:
        a = int(input("Give n: "))
    except:
        print("not int. quiting")
        quit()
    b = input("Give seed: ")
    print("generating list")
    random.seed(b)
    z = []
    for _ in range(a):
        z.append(random.randint(a=0, b=1000))
    print("generation done.")
    print("---------------------------")
    print("sorting...")
    z = mergeSort(z) #ah yeah, this overwrites your list, btw :3
    passed = checkIfSorted(z)
    if passed:
        print("TEST PASSED SUCCESSFULLY")
    else:
        print("FAILED!")

    

