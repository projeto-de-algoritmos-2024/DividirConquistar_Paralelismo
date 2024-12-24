import threading
import timeit
from baseinvertcount import *
import baseinvertcount


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


def threadedInvertionCount(this: list[int], count: int = 0):
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
    a = ThreadWithReturnValue(target=threadedInvertionCount, args=(this[:a], count))
    a.start()
    b = ThreadWithReturnValue(target=threadedInvertionCount, args=(this[a:], count))
    b.start()
    partA, countA = a.join()
    partB, countB = b.join()

    merged, sum = mergeCount(partA, partB, countA + countB)
    return merged, sum

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
    
