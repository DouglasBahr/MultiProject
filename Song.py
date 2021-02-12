#!/usr/bin/env python
# coding: utf-8

# In[7]:


# """
# Title: K-I-S-S-I-N-G song
# Date: 2021-02-11
# Author: Carl
# Description: this prints s in list to make a song
 
# """

# #Python import#e.g. from time import sleep
from time import sleep

#Custom imports  #e.g. from file import class as name

#Constants  # e.g. GENERIC_CONSTANT = "Status_Test_String"
LYRICS =\
"Carl and Sinthrill,\
Sittin' in a tree,\
K,\
I,\
S,\
S,\
I,\
N,\
G,\
First comes Love,\
Then comes Marriage,\
Then comes some very colourful verbiage."

lyrics_list = LYRICS.split(',')

#Code e.g. class Name():
for line in lyrics_list:
    print(line)
    sleep(0.6)



