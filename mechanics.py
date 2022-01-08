# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 22:44:34 2021

@author: Marcus T
"""

import numpy as np
from numba import njit

@njit(cache=True)
def checkForMatches(field, run_over, k):
    
    run_over_zoom = np.arange(3)
    
    # For each row in field, except first and last 
    for row in run_over:
        
        # For each column in field, except first and last
        for col in run_over:
            
            # Create zoomed field (3x3 box)
            zoomed_field = field[row-1:row+2, col-1:col+2]
            
            # Check rows for match
            for row_zoom in run_over_zoom:
                
                if (zoomed_field[row_zoom, 0] == 
                    zoomed_field[row_zoom, 1] == 
                    zoomed_field[row_zoom, 2]):
                    
                    
                    if zoomed_field[row_zoom, 0] != k+1:
                        # We had same items in entire row
                        field[row-1+row_zoom, col-1:col+2] = -2
                        return True
                    
            # Check columns for match
            for col_zoom in run_over_zoom:
                
                if (zoomed_field[0, col_zoom] == 
                    zoomed_field[1, col_zoom] == 
                    zoomed_field[2, col_zoom]):
                
                    if zoomed_field[0, col_zoom] != k+1:
                        # We had same items in entire column
                        field[row-1:row+2, col-1+col_zoom] = -1
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