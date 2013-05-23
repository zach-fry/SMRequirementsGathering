'''
@author Zach Fry (fryz)
@date 2/21/2013

example located at test/genvisTest/example.py
'''

import os
import json
import codecs
from itertools import combinations

#hashtag_dirs = '/home/fryz/twitter_crawler/results/Feb10/'

'''
These loadXList functions load in a list of object X to filter tweets by
X in this case can be users or hashtags
'''
def loadHashtagList(hashtag_path, hashtag_list):
    f = open(hashtag_path, 'r')
    for line in f:
        hashtag_list.append(line.strip())
    f.close()

def loadUserList(user_path, user_list):
    f = open(user_path, 'r')
    for line in f:
        user_list.append(line.strip())
    f.close()

'''
This function calculates hashtag occurences
 - hashtag_dirs is directory containing raw twitter JSON files
 - hashtag_list is optional list of hashtags to filter on
 - hashtag_counts is unigram hashtag occurence in form of {tag:freq}
    - output parameter 
 - hashtag_link_counts is bigram hashtag occurence in form of {tag:{tag:freq}}
    - output parameter
'''
def loadHashtagCounts(hashtag_dirs, hashtag_counts, hashtag_link_counts, hashtag_list=[]):
    for tag_dir in os.listdir(hashtag_dirs):
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
                    tags = sorted(tags)

                    if len(hashtag_list) > 0:
                        intersect_list = [val for val in tags if val in hashtag_list]
                        tags = sorted(intersect_list)
                    
                    #pass an empty dict for hashtag_counts if you want unigram tag occurence
                    if hashtag_counts is not None:
                        for tag in tags:
                            if tag in hashtag_counts:
                                hashtag_counts[tag] += 1
                            else:
                                hashtag_counts[tag] = 2
                    #pass and empty dict for hashtag_link_counts if you want bigram tag occurences
                    if hashtag_link_counts is not None:
                        for i,j in combinations(tags, 2):
                            if i in hashtag_link_counts:
                                if j in hashtag_link_counts[i]:
                                    hashtag_link_counts[i][j] += 1
                                else:
                                    hashtag_link_counts[i][j] = 1
                            else:
                                hashtag_link_counts[i] = {j : 1}

'''
This function calculates hashtag occurences by users
 - hashtag_dirs is directory containing raw twitter JSON files
 - hashtag_list is optional list of hashtags to filter on
 - user_list is optional list of users to filter on
 - user_tagdict_map is a {user:{tag:freq}} dictionary that will be returned
    - output parameter
'''
def loadUserTagMap(hashtag_dirs, user_tagdict_map, hashtag_list=[], user_list=[]):
    for tag_dir in os.listdir(hashtag_dirs):
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
                    tags = sorted(tags)
                    
                    if len(hashtag_list) > 0:
                        intersect_list = [val for val in tags if val in hashtag_list]
                        tags = sorted(intersect_list)

                    user = r['from_user']
                    if len(user_list) > 0:
                        if user not in user_list: pass
                        else:
                            if user not in user_tagdict_map:
                                user_tagdict_map[user] = {}
                            for tag in tags:
                                if tag not in user_tagdict_map[user]:
                                    user_tagdict_map[user][tag] = 1
                                else:
                                    user_tagdict_map[user][tag] += 1
                    else:
                        if user not in user_tagdict_map:
                            user_tagdict_map[user] = {}
                        for tag in tags:
                            if tag not in user_tagdict_map[user]:
                                user_tagdict_map[user][tag] = 1
                            else:
                                user_tagdict_map[user][tag] += 1

'''
This Function writes a {user : {tag:freq}} dict to a csv file named usertags.csv
 - user_tagdict_map come from calling loadUserTagMap
 - outpath is dir that file will be written to
'''
def writeCSV(user_tagdict_map, outpath='.'):
    hashtag_list = []
    for user,tagdict in user_tagdict_map.iteritems():
        hashtag_list.extend([x for x in tagdict.keys() if x not in hashtag_list])

    f = open('%s/usertags.csv'%outpath, 'w')
    f.write('user,%s\n'%(','.join(hashtag_list)))

    for user in user_tagdict_map.keys():
        counts = []
        for tag in hashtag_list:
            if tag in user_tagdict_map[user]: counts.append(user_tagdict_map[user][tag])
            else: counts.append(0)
    
        f.write('%s,%s\n'%(user,','.join([str(x) for x in counts])))
    f.close()

'''
This function creates a JSON file for displaying a wordcloud of hashtags for d3.js
'''
def writeHashtagWordCloudJSON(hashtag_counts, hashtag_list=[], outpath='.'):
    jobj = []
    if len(hashtag_list) > 0:
        for hashtag in hashtag_list:
            td = {}
            td["name"] = hashtag
            td["value"] = hashtag_counts[hashtag]
            jobj.append(td)
    else:
        for hashtag, freq in hashtag_counts.iteritems():
            td = {}
            td["name"] = hashtag
            td["value"] = freq
            jobj.append(td)
    f = open('%s/hashtag_wordcloud.json'%outpath, 'w')
    json.dump(jobj, f)
    f.close()
 
'''
This function creates a JSON file for displaying a wordcloud of users for d3.js
'''
def writeUserWordCloudJSON(user_tagdict_map, user_list=[], outpath='.'):
    jobj = []
    if len(user_list) > 0:
        for user in user_list:
            td = {}
            td["name"] = user
            td["value"] = sum( user_tagdict_map[user].values() )
            jobj.append(td)
    else:
        for user,tagdict in user_tagdict_map.iteritems():
            td = {}
            td["name"] = user
            td["value"] = sum( tagdict.values() )
            jobj.append(td)
    f = open('%s/user_wordcloud.json'%outpath, 'w')
    json.dump(jobj, f)
    f.close()

'''
This Function writes a {tag : {tag:freq}} dict to a JSON file
that gets rendered as a Hashtag X Hashtag Matrix
 - hashtag_link_counts comes from calling loadHashtagCounts
 - hashtag_list is list of hashtags that form the rows and columns of the matrix
 - outpath is dir that file will be written to
'''
def writeSymmetricCoOccurenceJSON(hashtag_link_counts, hashtag_list=[], outpath='.'):
    if len(hashtag_list) == 0:
        hashtag_list = hashtag_link_counts.keys()
        for tag in hashtag_link_counts.keys():
            for tag2 in hashtag_link_counts[tag].keys():
                if tag2 not in hashtag_list: hashtag_list.append(tag2)

    d = {'nodes':[], 'links':[]}
    for tag in hashtag_list:
        td = {}
        td['name'] = tag
        td['group'] = 1
        d['nodes'].append(td)

    for i,tag1 in enumerate(hashtag_list):
        try:
            for tag2,freq in hashtag_link_counts[tag1].iteritems():
                j = hashtag_list.index(tag2)
                td = {}
                td['source'] = i
                td['target'] = j
                td['value'] = freq
                d['links'].append(td)
        except KeyError:
            pass

    f = open('%s/co_tag.json'%outpath, 'w')
    json.dump(d, f)
    f.close()   

'''
This Function writes a {user : {tag:freq}} dict to a JSON file
that gets rendered as a Hashtag X User Matrix
 - user_tagdict_map come from calling loadUserTagMap
 - hashtag_list is list of hashtags that form the rows of the matrix
 - user_list is list of users that form the columns of the matrix
 - outpath is dir that file will be written to
'''
def writeAsymmetricCoOccurenceJSON(user_tagdict_map, hashtag_list, user_list, outpath='.'):
    d = {'tags':[], 'users':[], 'links':[]}
    for tag in hashtag_list:
        td = {}
        td['tag'] = tag
        td['group'] = 1
        d['tags'].append(td)

    for user in user_list:
        td = {}
        td['name'] = user
        td['group'] = 1
        d['users'].append(td)

    for i,tag in enumerate(hashtag_list):
        for j,user in enumerate(user_list):
            if user not in user_tagdict_map: pass
            elif tag not in user_tagdict_map[user]: pass
            else:
                td = {}
                td['toTag'] = i
                td['fromUser'] = j
                td['value'] = user_tagdict_map[user][tag]
                d['links'].append(td)

    f = open('%s/co_tag_user.json'%outpath, 'w')
    json.dump(d, f)
    f.close()
