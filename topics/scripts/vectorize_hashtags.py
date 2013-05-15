'''
@author Zach Fry (fryz)
@date 4/28/2013
'''

import os
import json
import codecs

hashtag_dir = '/home/fryz/FirstResponder/twitter_crawler/results/Feb10/'
vector_dir = '/home/fryz/FirstResponder/topics/vectors/'

def loadTweets(hashtag_dirs, tweet_dict):
    print 'loading tweets'
    index = 0
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
                    tweet_dict[index] = tags 
                    index += 1

def writeVectorsToFile(vector_dir, tweet_dict):
    print 'writing tweets'
    for i,hashtags in tweet_dict.iteritems():
        f = codecs.open('%s/%s.txt'%(vector_dir, i), 'w', 'utf8')
        for hashtag in hashtags:
            f.write('%s\n'%hashtag)
        f.close()

'''
This function adds to the stopwords any 
    hashtags found in > 25% of all tweets
    hashtags that occur <= 3 times in all tweets
'''
def getStopWords(tweet_dict, stop_words, write=False):
    print 'getting stopwords'
    document_dict = {}
    num_docs = len(tweet_dict.keys())
    for doc_id, hashtags in tweet_dict.iteritems():
        for hashtag in hashtags:
            if hashtag not in document_dict: document_dict[hashtag] = []
            if doc_id not in document_dict[hashtag]:
                document_dict[hashtag].append(doc_id)
    
    for hashtag, docs in document_dict.iteritems():  
        freq = len(docs)
        if float(freq)/float(num_docs) > 0.25 or freq <= 3:
            stop_words.append(hashtag)
    
    if write == True:
        f = codecs.open('stopwords.txt', 'w', 'utf8')
        for each in stop_words:
            f.write('%s\n'%each)
        f.close()

tweet_dict = {}
loadTweets(hashtag_dir, tweet_dict)
getStopWords(tweet_dict, [], write=True)
writeVectorsToFile(vector_dir, tweet_dict)
