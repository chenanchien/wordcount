# -*- coding: utf-8 -*-

from operator import itemgetter
import re
facebook = open("facebook.txt","r",encoding = "utf-8")

word_list = {}

for line in facebook:
    words = re.split('\W+',line)
    for word in words:
        if word in word_list:
            word_list[word] += 1
        else:
            word_list[word] = 1

best = sorted(word_list.items(),key = itemgetter(0))
for i in best:
    print(i)



maxlen = 0
maxword = ""
for j in word_list:
    if len(j) > maxlen:
        maxlen = len(j)
        maxword = j
        print(j, len(j))

facebook.close()