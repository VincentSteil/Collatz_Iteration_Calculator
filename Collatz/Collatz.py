#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing (professor) & Vincent Steil 
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

def collatz_eval (i, j, cache):
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    cache is an overarching dict of cycle lengths for each index, initialized at 0 
    start at count c = 1 to account for first number
    """
    assert i > 0
    assert j > 0
    v = 0

    for k in xrange(min(i,j),(max(i,j)+1)):
        l = collatz_cyclelength(k, cache)   
        v = max(v,l)  
    assert v > 0
    return v

# -------------
# collatz_cyclelength
# -------------

def collatz_cyclelength (n, cache, c = 1):
    """
    n is the number for which the cycle length should be computed
    returns the cycle length
    n even : /2
    n odd : *3 +1
    check cache for precomputed values
    c is count
    """
    assert n > 0
    if n != 1:
        if n in cache :
          return cache[n]
        else :
            if n % 2 == 0 :
                cache[n/2] = collatz_cyclelength (n/2, cache, c)
                c = c + cache[n/2]
                assert c > 0
                return c
            else :
                cache[3*n + 1] = collatz_cyclelength(3*n + 1, cache, c)
                c = c + cache[3*n + 1]
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
    cache is an dictionary with precalculated collatz iteration values used to successively speed up later calculations
    """
    cache = {}
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1], cache)
        collatz_print(w, a[0], a[1], v)
