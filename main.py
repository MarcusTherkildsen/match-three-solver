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
old_field = np.copy(field)
#print(field)
runs = 0
while checkForMatches(field, run_over_full, k):
    
    if (runs % 20) == 0:
    
        print(f'Plotting after {runs} runs')    
    
        # Get the negative coordinates, for color-plotting
        neg_idx = np.where(field < 0)
        
        plt.figure()
        plt.matshow(old_field, vmin=-2, vmax=k+1)
        plt.plot(neg_idx[1], neg_idx[0],'-*', color='r')
        plt.show()

     
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



tmp = np.where(field == k+1)
tmp_len_tmp = len(tmp[0])


tmp_len.append(tmp_len_tmp)

if tmp_len_tmp == n*n:
    print(f'For n_total: {n_total} a complete solution was found')
    exit

'''
psuedo code time


Step 2

if reach_able_match in zoombox:
    reach it

    restart loop from top

'''


