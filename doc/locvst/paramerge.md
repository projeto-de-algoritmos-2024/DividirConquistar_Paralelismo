### Introduction - what is this document
    This document explains the thought process behind implementing 
    the paralel merge 

### multithreading vs. multiprocessing approach

    According to the video i'm following to simply learn how to use python's
    threading library, threading is not very useful for cpu-bound processes, 
    he didn't exactly expand on the why or how. 
    Anyway, for our purposes, it would be useful to take a look at both approaches
    considering the merge may be modeled as such:
    1. We make our child accountable for returning the sorted out parts
    2. then we merge it out.
    And this "making our child accountable" might also translate to something like
    creating a thread and waiting for it to join.

### Expected function changes
    The way I look at it, actually getting a return value or pointer from the thread would
    imply much more investment than return. Theeeen we could simply pass a pointer to the function
    and get our return value from such a return. That seems more like it.
    And that's precisely what i'll try. 

    If all fails, I'll stop using the "threading" and go to concurrency.future, which supposedly 
    does precisely the same, but in a supposed simpler way. 
    That said, simpler my Bravo Alpha, we may need more lines of code to use threading, but the advantage
    is very clear: code clarity! And you better believe code clarity is hella important when dealing with
    a team job, meaning this job!!!

###