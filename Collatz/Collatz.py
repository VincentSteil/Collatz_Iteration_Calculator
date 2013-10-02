#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing & Vincent Steil 
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

def collatz_eval (i, j, cache) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    cache is an overarching list of cycle lengths for each index, initialized at 0
    """
    assert i > 0
    assert j > 0
    assert len(cache) > 0
    v = 0

    for k in xrange(min(i,j),(max(i,j)+1)) :
        l = collatz_cyclelength(k, cache)   
        v = max(v,l)  
    assert v > 0
    return v

# -------------
# collatz_cyclelength
# -------------

def collatz_cyclelength (n, cache):
    """
    n is the number for which the cycle length should be computed
    returns the cycle length
    start at c = 1 to account for first number
    n even : /2
    n odd : *3 +1
    check cache for 
    """
    assert n > 0
    assert len(cache) > 0
    c = 1
    if (n != 1) and (n < 333330) :
        if cache[n] != 0 :
          return cache[n]
        else :
            if n % 2 == 0 :
                cache[n/2] = collatz_cyclelength (n/2, cache)
                c = c + cache[n/2]
                assert c > 0
                return c
            else :
                cache[3*n + 1] = collatz_cyclelength(3*n + 1, cache)
                c = c + cache[3*n + 1]
                assert c > 0
                return c
    elif n != 1 :
        if (n % 2 == 0) and (n/2 < 999999):
                cache[n/2] = collatz_cyclelength (n/2, cache)
                c = c + cache[n/2]
                assert c > 0
                return c
        elif n % 2 == 0 :
                c = c + collatz_cyclelength(n/2, cache)
                assert c > 0
                return c
        elif 3*n + 1 < 999999 :
                cache[3*n + 1] = collatz_cyclelength(3*n + 1, cache)
                c = c + cache[3*n + 1]
                assert c > 0
                return c 
        else :
                c = c + collatz_cyclelength(3*n + 1, cache)
                assert c > 0
                return c
    
    else :
        cache[1] = 1
        return 1   
        


# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    cache is an array with precalculated collatz iteration values used to successively speed up later calculations
    """
    cache = [0] * 1000000
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1], cache)
        collatz_print(w, a[0], a[1], v)
