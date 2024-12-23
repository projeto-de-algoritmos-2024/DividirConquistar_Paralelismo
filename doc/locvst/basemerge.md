This documentation on the basemergesort was written by bcl0c 

### Introduction - what is this foxtrot document
    This document is basic commentary and expectations on mergesort

### On the performance
    Surprisingly fast. Almost didn't leave me waiting to sort 100k random numbers. 
    And verifier also runned blazingly fast, almost instant, specially considering 
    process was using no more than 10% of the available processing power.

    Shame it very much did leave me waiting until i gave up when i tried sorting a
    random array of about a million numbers or so. Not very great, but i guess it might as
    well be a python issue moment. Or it was trying to swap out or something. Maybe, maybe. 
    I have no clue on why it took so long. 

### On the implementation  
    This algorithm, thank God, is very intuitive.
    Sort the parts, merge the parts, get something sorted
    as a result.
    Not bad at all.

### On the paralelization
    I'll be doing that next, so have no comments as of 23122024_1613

