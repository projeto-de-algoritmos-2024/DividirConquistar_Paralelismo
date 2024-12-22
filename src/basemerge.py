"""
Written by bcl0c.

Warning ZERO: violence :>

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


def merge(partA: list[int], partB: list[int]) -> list[int]:
    res = []
    while len(partA) > 0:
        if partA[0] < partB[0]: #partA always greater or equal in length
            res.append(partA.pop(0))
        res.append(partB.pop(0))
    while len(partA) > 0: #if MikeFoxtroting partB ends, copy rest of A already.
        res.append(partA.pop(0))

def mergeSort(this: list[int]):
    a = len(this)
    a
    pass