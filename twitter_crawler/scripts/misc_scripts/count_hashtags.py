'''
@author Zach Fry (fryz)
@date 2/10/2013
'''

import os
import json
from itertools import combinations
import codecs

vocab_map = {}
occurence_map = {}
bigram_occurence_map = {}
index = 0

hashtag_dirs = '/home/fryz/twitter_crawler/results/'
for tag_dir in os.listdir(hashtag_dirs):
    for results in os.listdir(hashtag_dirs+tag_dir):
        fname = hashtag_dirs+tag_dir+'/'+results
        if results == 'maxid.txt': pass
        else:
            f = codecs.open(fname, 'r', 'utf8')
            json_obj = json.load(f)
            f.close()
            print fname
            for r in json_obj['results']:
                tags = [ x['text'].lower() for x in r['entities']['hashtags'] ]
                tags = sorted(tags)

                for tag in tags:
                    if tag in vocab_map:
                        i = vocab_map[tag]
                        occurence_map[i] += 1
                    else:
                        vocab_map[tag] = index
                        occurence_map[index] = 1
                        index += 1

                for bigram in combinations(tags, 2):
                    i = vocab_map[bigram[0]]
                    j = vocab_map[bigram[1]]
                    if i in bigram_occurence_map:
                        if j in bigram_occurence_map[i]:
                            bigram_occurence_map[i][j] += 1
                        else:
                            bigram_occurence_map[i][j] = 1
                    else:
                        bigram_occurence_map[i] ={j : 1}

                    #if j in bigram_occurence_map:
                        #if i in bigram_occurence_map[j]:
                            #bigram_occurence_map[j][i] += 1
                        #else:
                            #bigram_occurence_map[j][i] = 1
                    #else:
                        #bigram_occurence_map[j] = {i : 1}

inv_vocab_map = dict((v,k) for k,v in vocab_map.iteritems())

f = codecs.open('/home/fryz/twitter_crawler/stats/hashtags.counts', 'w', 'utf8')
for k,v in occurence_map.iteritems():
    f.write('%s\t%s\n'%(inv_vocab_map[k],v))
f.close()

f = codecs.open('/home/fryz/twitter_crawler/stats/hashtags.links', 'w', 'utf8')
for k,v in bigram_occurence_map.iteritems():
    for k2,v2 in v.iteritems():
        f.write('%s\t%s\t%s\n'%(inv_vocab_map[k], inv_vocab_map[k2], v2))
f.close()

