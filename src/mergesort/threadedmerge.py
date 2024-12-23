
import threading
import timeit
from basemerge import *

# -------------------------------//---------------------------------
# some stackoverflow code for helping not having to reinvent the wheel again :3
def split_list(list, wanted_parts=1):
    length = len(list)
    return [ list[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]
class ThreadWithReturnValue(threading.Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return
# -------------------------------//---------------------------------


# now comes the threadification of the code:
def divide(list= list[int], threads= int):
    size = len(list)
    if size >= threads:
        new_lists = split_list(list, threads) # it divides the list for each thread to take a slice of the cake
        lists = []
        aux = 0
        while aux < len(new_lists)-1: # it creates threads in the value we extipulated :P
            a = ThreadWithReturnValue(target=divide, args=([new_lists[aux]], threads))
            a.start()
            b = ThreadWithReturnValue(target=divide, args=([new_lists[aux+1]], threads))
            b.start()
            lists.append(merge(a.join(), b.join()))
            aux += 2 # i almost fucked up my computer lol i hate while loops

        return conquer(lists)
    else:
        return mergeSort(list)

def conquer(lists): # this is basically the mergesort again, but this time it only merges and finish off our process
    lenght = len(lists)
    if lenght == 1:
        return lists[0]
    lenght = int(lenght/2)
    for i in range(lenght):
        return merge(conquer(lists[:lenght]), conquer(lists[lenght:]))



def checkIfSorted(somelist: list[int]):
    
    for i in range(len(somelist) - 1):
        if somelist[i] > somelist[i+1]:
            return False
    else:
        return True
    
#this is TheGreat test routine. It actually tests the mergeSort.

def list_generation(a,b):
    print("generating list")
    random.seed(b)
    z = []
    for _ in range(a):
        z.append(random.randint(a=0, b=1000))
    print("generation done.")
    return z


if __name__ == "__main__":
    print("STARTING thegreat TEST ROUTINE!")
    import random
    try:
        a = int(input("Give n: "))
    except:
        print("not int. quiting")
        quit()
    b = input("Give seed: ")
    
    z = list_generation(a,b)


    print("---------------------------")
    print("sorting...")
    start = timeit.default_timer()
    x = divide(z, 8) # threaded
    stop = timeit.default_timer()
    print('Threaded Time: ', stop - start)
    passed = checkIfSorted(x)
    if passed:
        print("TEST PASSED SUCCESSFULLY")
    else:
        print("FAILED!")
    

    print("---------------------------")
    print("sorting...")
    start = timeit.default_timer()
    y = mergeSort(z) #ah yeah, this overwrites your list, btw :3   it doesn't anymore >:)
    stop = timeit.default_timer()
    print('Normal Time: ', stop - start)
    passed = checkIfSorted(x)
    if passed:
        print("TEST PASSED SUCCESSFULLY")
    else:
        print("FAILED!")

