"""
Written by bcl0c. Violence!!!!

This code is basically the same as basemerge, but merge now spawns his devil children
to do his dirty work, very great song by steely dan, btw.

"""
import basemerge
import threading

THREADS = 8

def merge(partA: list[int], partB: list[int], res: list) -> list[int]: #works for even stupid ass big numbers somewhat fast.
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

def mergeSort(this: list[int], res: list) -> None:

    #as with simple single thread version,
    #this -> list to be sorted; but
    #res -> pointer to where you expect the result to be.
    #major break condition
    if threading.activeCount() >= THREADS:
        sorted = basemerge.mergeSort(this)
        print("sorted: ", sorted)
        for item in sorted:
            res.append(item)
        return
    #minor break condition
    if len(this) == 1:
        #then, res gets a copy.
        res.append(this[0]) #simple as.
        return
    a = len(this)
    a = a//2 

    #same here, 
    partA = []
    partB = []
    t1 = threading.Thread(target=mergeSort, args=[this[:a], partA])
    t2 = threading.Thread(target=mergeSort, args=[this[a:], partB])
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # can't exactly be paralelized, yet it kinda is, since
    # we can assume this is also running on a thread or process.
    merge(partA, partB, res)


def checkIfSorted(somelist):
    
    for i in range(len(somelist) - 1):
        if somelist[i] > somelist[i+1]:
            return False
    else:
        return True

def veryMinorTest():
    print("STARTING mini TEST ROUTINE!")

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
    new = []
    z = basemerge.mergeSort(z) #ah yeah, this overwrites your list, btw :3 (i do think so, at least)

    print("------------")
    print("sorted: ", z)
    print("-------------") 

    passed = checkIfSorted(z)
    if passed:
        print("TEST PASSED SUCCESSFULLY")
    else:
        print("FAILED!")

def minorTest():
    print("STARTING minor TEST ROUTINE!")
    print("-----------------------------")
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
    z = []
    print("---------OG----------")
    print(list1)
    print(list2)
    print(z)
    print("---------------------")

    
    merge(list1, list2, z)
    print("---------NEW---------")
    print(z)
    print("-------------------")

def majorTest():
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
    new = []
    mergeSort(z, new) #ah yeah, this overwrites your list, btw :3 (i do think so, at least)
    """ 
    print("------------")
    print("unsorted: ", z)
    print("sorted: ", new)
    print("-------------") 
    """

    passed = checkIfSorted(new)
    if passed and len(new) == len(z):
        print("TEST PASSED SUCCESSFULLY")
    else:
        print("FAILED!")


#this is TheGreat test routine. It actually tests the mergeSort.
if __name__ == "__main__":
    majorTest()

