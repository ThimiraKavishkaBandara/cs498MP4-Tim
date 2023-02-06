#!/usr/bin/env python3
import sys


tlist = []
# # input comes from STDIN
# for line in sys.stdin:
#     # TODO
#     line = line.strip()
#     wordCount= line.split('\t',1)
#     tlist.append(wordCount)
# top5 = tlist[0:10]
# for item in top5:
#     print('%s\t%s' % (item[0],item[1]))
    
    # print('%s\t%s' % (  ,  )) print as final output

for line in sys.stdin:
    # TODO
    line = line.strip()
    count,word = line.split('\t',1)
    tlist.append([int(count),word])

tlist.sort()

for page in tlist:
    print('%s\t%s' % (page[1],page[0]))
    # print('%s\t%s' % (  ,  )) print as final output