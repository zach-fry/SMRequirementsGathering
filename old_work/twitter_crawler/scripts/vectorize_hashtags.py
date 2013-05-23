'''
@author Zach Fry (fryz)
@date 2/10/2013
'''

import os
import json
from itertools import combinations
import codecs

index = 0
vector_dir = '/home/fryz/hashtag_vectors/'

hashtag_dirs = '/home/fryz/twitter_crawler/results/Feb10/'
for tag_dir in os.listdir(hashtag_dirs):
    print tag_dir
    for results in os.listdir(hashtag_dirs+tag_dir):
        fname = hashtag_dirs+tag_dir+'/'+results
        if results == 'maxid.txt': pass
        else:
            f = codecs.open(fname, 'r', 'utf8')
            json_obj = json.load(f)
            f.close()
            #print fname
            for r in json_obj['results']:
                tags = [ x['text'].lower() for x in r['entities']['hashtags'] ]
                for tag in tags:
                    if os.path.exists('%s%s.txt'%(vector_dir,index)):
                        f = codecs.open('%s%s.txt'%(vector_dir,index), 'a', 'utf8')
                        f.write('%s\n'%(tag))
                        f.close() 
                    else:
                        f = codecs.open('%s%s.txt'%(vector_dir,index), 'w', 'utf8')
                        f.write('%s\n'%(tag))
                        f.close() 
                index += 1

print 'There are %s feature vectors'%index
