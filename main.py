# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 23:16:56 2021

@author: Marcus T
"""

import numpy as np
from mechanics import checkForMatches, moveDown, fillInNewEntries
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
This script serves to solve a candy crush clone game, the fastest possible way
"""


'''
The game - 
consists of a n by n playing field with k possible unique items
'''

n = 15
k = 3#int(n/4)

n_total = 10#n*n*2
    
#np.random.seed(seed=8)#)4)

tmp_len = []

#from tqdm import trange

i = 1

np.random.seed(seed=i)

print(f'Running with i: {i}')
#for n_total in [20]:#trange(100, desc='Running n_total series..'):
    
    
'''
todo
N=5
K=3
N_TOTAL = 2
SEED = 8

WITH IF ON FILLINNEW
'''

field = (np.random.randint(low=0, high=k, size=n*n)).reshape(n, n)

'''
Now check for first available move that will enable three connected pieces
'''

run_over = np.arange(n-2)+1

run_over_full = range(n)
run_over_full_reversed = np.flip(run_over_full)


'''
psuedo code time


Step 1

if match in zoombox:
    count down match
    delete match
    move down
    fill in new entries in top
    
    restart loop from top
'''


'''

THIS IS BASICALLY JUST PREPARING THE PLAYING FIELD 

'''

old_field = np.copy(field)
#print(field)
runs = 0
while checkForMatches(field, run_over_full, k):
    
    if (runs % 100) == 0:
    
        print(f'Plotting after {runs} runs')    
    
        # # Get the negative coordinates, for color-plotting
        # neg_idx = np.where(field < 0)
        
        # plt.figure()
        # plt.matshow(old_field, vmin=-2, vmax=k+1)
        # plt.plot(neg_idx[1], neg_idx[0],'-*', color='r')
        # plt.show()

     
    runs += 1
    
    # Count down match
    #n_total -= 3

    # Move everything down that can be moved
    while moveDown(field, run_over_full, run_over_full_reversed, k):
        pass
    
    if n_total > 0:
        #print(n_total)
        fillInNewEntries(field, run_over_full, k)
    
    old_field = np.copy(field)
    
#print(f'Run: {runs}')
    
#print(field)


plt.figure()
plt.matshow(old_field, vmin=-2, vmax=k+1)
plt.show()

'''
NOW THE PLAYING FIELD IS READY, ACTUALLY PLAY


The idea is to go through vertically first. 

1) Check if any two adjacent fields in a row can be exchanged to get 3 matches
    If yes, do that

2) Check the row directly above and directly below

'''

match_n = 2

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
                    # Check if switching neighbouring values will do anything
                    
                    '''
                    Check left hand side
                    '''
                    
                    leftmost_idx = col-cnt
                    
                    if leftmost_idx > 1:
                        # Means the leftmost is not at 1st entry, 
                        # thus we can check if switching the two entries to the left will result in a match
                
                        # Checking value two steps away
                        leftmost_value = field[row, leftmost_idx-2]
                        
                        if leftmost_value == last:
                            # We will get a match if we switch these
                            # So do it

                            field[row, col-cnt-2] = field[row, col-cnt-1]
                            field[row, col-cnt-1] = leftmost_value
                            
                            #marcus break here and return to the loop that checks for matches
                            
                            break
                        
                    '''
                    Check right hand side
                    '''
                    
                    rightmost_idx = col-1
                    
                    if rightmost_idx < (n-2):
                        # Means the rightmost is not at 2nd last entry, 
                        # thus we can check if switching the two entries to the right will result in a match
                
                        # Checking value two steps away
                        rightmost_value = field[row, rightmost_idx+2]
                        
                        if rightmost_value == last:
                            # We will get a match if we switch these
                            # So do it

                            field[row, rightmost_idx+2] = field[row, rightmost_idx+1]
                            field[row, rightmost_idx+1] = rightmost_value
                    
                            #marcus break here and return to the loop that checks for matches
                    
                            break
                        
                    # TODO need to check if there are any rows above or below, otherwise we cannot do this 
                                     
                    '''
                    Check if we can get a match from above on the left side
                    '''         
                    
                    if (leftmost_idx > 0) and (row != 0):
                    
                        # Means the leftmost is not at 1st entry, 
                        # thus we can check if switching with the value one step to the left and one step up will give a match
                
                        leftmost_value = field[row-1, leftmost_idx-1]
                        
                        if leftmost_value == last:
                            # We will get a match if we switch these
                            # So do it

                            field[row-1, leftmost_idx-1] = field[row, leftmost_idx-1]
                            field[row, leftmost_idx-1] = leftmost_value
                        
                            break
                    
                    
                    '''
                    Check if we can get a match from below on the left side
                    '''
                    
                    if (leftmost_idx > 0) and (row != (n-1)):
                    
                        # Means the leftmost is not at 1st entry, 
                        # thus we can check if switching with the value one step to the left and one step down will give a match
                
                        leftmost_value = field[row+1, leftmost_idx-1]
                        
                        if leftmost_value == last:
                            # We will get a match if we switch these
                            # So do it

                            field[row+1, leftmost_idx-1] = field[row, leftmost_idx-1]
                            field[row, leftmost_idx-1] = leftmost_value
                        
                            break
                        
                        
                    '''
                    Check if we can get a match from above on the right side
                    '''         
                    
                    if (rightmost_idx < (n-1)) and (row != 0):
                    
                        # Means the rightmost is not at last entry, 
                        # thus we can check if switching with the value one step to the right and one step up will give a match
                
                        rightmost_value = field[row-1, rightmost_idx+1]
                        
                        if rightmost_value == last:
                            # We will get a match if we switch these
                            # So do it

                            field[row-1, rightmost_idx+1] = field[row, rightmost_idx+1]
                            field[row, rightmost_idx+1] = rightmost_value
                        
                            break
                    
                    
                    '''
                    Check if we can get a match from below on the right side
                    '''
                    
                    if (rightmost_idx < (n-1)) and (row != (n-1)):
                    
                        # Means the rightmost is not at last entry, 
                        # thus we can check if switching with the value one step to the right and one step down will give a match
                
                        rightmost_value = field[row+1, rightmost_idx+1]
                        
                        if rightmost_value == last:
                            # We will get a match if we switch these
                            # So do it

                            field[row+1, rightmost_idx+1] = field[row, rightmost_idx+1]
                            field[row, rightmost_idx+1] = rightmost_value
                        
                            break
                        
                cnt = 1
                last = cur
                    
plt.figure()
plt.matshow(field, vmin=-2, vmax=k+1)
#plt.grid()
plt.show()

# # Search for vertical matches
# for col in run_over:
#     cur = -1
#     last = -2
#     cnt = 0
 
#     for row in run_over:
#         cur = field[row, col]
        
#         if cur == k+1:
#             # Skip
#             cnt = 0
#             pass
#         else:
        
#             if cur == last:
#                 cnt += 1
#             else:
    
#                 if cnt >= match_n:
#                     # Means that the previous n+ were equal but the current one isn't
#                     # Mark them
#                     field[row-cnt:row, col] = -1
 
                
#                 cnt = 1
#                 last = cur
    
#     if cnt >= match_n:
#         # Means we went to last entry and the previous n+ were equal
#         # Mark them
#         field[row+1-cnt:, col] = -1

    





