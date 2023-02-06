#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO
curr_word = None                                          
curr_count = 0                                             
# res = {}
res = []
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word, count = line.split("\t",1)
    count = int(count)

    if curr_word == word:                                  
        curr_count = curr_count + count                               
    else:
        if curr_word:
             res.append((curr_word , curr_count )) 
             #print('%s\t%s' % (curr_word , curr_count )) 
        curr_word = word                                   
        curr_count = count                               
        
if curr_word == word: 
    res.append((curr_word , curr_count ))                                     
    #print('%s\t%s' % (curr_word,curr_count))


#sorted_res = list(sorted(res, key = lambda x: (-x[1],x[0])))                  
sorted_res2 = list(sorted(res, key = itemgetter(1)))
sorted_res2.reverse()

for item in sorted_res2:
    print('%s\t%s' % (item[0],item[1]))





# print('%s\t%s' % (  ,  )) print as final output