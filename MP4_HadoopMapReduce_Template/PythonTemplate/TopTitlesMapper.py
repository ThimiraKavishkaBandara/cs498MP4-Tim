#!/usr/bin/env python3
import sys


# TODO

# res = []
# alist = []
# for line in sys.stdin:
#        line = line.strip()
#        word, count = line.split('\t',1)
# #        res.append(word, count)

# # sorted_res = sorted()

# #TODO
#        print('%s\t%s' % (word , count)) 


count = 10
top_words = []

for line in sys.stdin:
    line = line.strip()
    if count > 0:
        top_words.append(line)
    count = count - 1

top_words.reverse()
for elem in top_words:
    word, count = elem.split('\t',1)
    print('%s\t%s' % (count,word))
