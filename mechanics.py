# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 22:44:34 2021

@author: Marcus T
"""

import numpy as np
from numba import njit

#@njit(cache=True)
def checkForMatches(field, run_over, k):
    
    match_n = 3

    # Search for horizontal matches
    for row in run_over:
        cur = -1
        last = -2
        cnt = 0

        for col in run_over:
            cur = field[row, col]
            
            if cur == k+1:
                # Skip
                cnt = 0
                pass
            else:
                
                if cur == last:
                    cnt += 1
                else:
    
                    if cnt >= match_n:
                        # Means that the previous n+ were equal but the current one isn't
                        # Mark them
                        field[row, col-cnt:col] = -1
                        return True
                    
                    cnt = 1
                    last = cur
    
        if cnt >= match_n:
            # Means we went to last entry and the previous n+ were equal
            # Mark
 #           marcus sæt breakpoint her og kig på det.. ses 
            field[row, col+1-cnt:] = -1
            return True

    # Search for vertical matches
    for col in run_over:
        cur = -1
        last = -2
        cnt = 0

        for row in run_over:
            cur = field[row, col]
            
            if cur == k+1:
                # Skip
                cnt = 0
                pass
            else:
            
                if cur == last:
                    cnt += 1
                else:
    
                    if cnt >= match_n:
                        # Means that the previous n+ were equal but the current one isn't
                        # Mark them
                        field[row-cnt:row, col] = -1
                        return True
                    
                    cnt = 1
                    last = cur
    
        if cnt >= match_n:
            # Means we went to last entry and the previous n+ were equal
            # Mark them
            field[row+1-cnt:, col] = -1
            return True

    return False

#@njit(cache=True)
def moveDown(field, run_over_full, run_over_full_reversed, k):

    for col in run_over_full:

        for row in run_over_full_reversed:
            if field[row, col] < 0:
                # Move all entries that are above 1 down, exit loop and rerun 
                # from the start
                
                #print(field[:, col])
                
                if row != 0:

                    entries_above = field[:row, col]
                    len_entries_above = len(entries_above)
                    
                    # Move the entries 1 step down
                    field[1:len_entries_above+1, col] = entries_above
                    
                # Indicate which entries to create new items for
                field[0, col] = k+1
                #print(field[:, col])
                
                return True

    return False

#@njit(cache=True)
def fillInNewEntries(field, run_over_full, k):

    for col in run_over_full:
        for row in run_over_full:
            if field[row, col] == k+1:
                # Found an entry that needs replacing
                #print(field[:, col])
                field[row, col] = np.random.randint(low=0, high=k, size=1)
                #print(field[:, col])
            else:
                break