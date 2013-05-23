import csv
import re

hashtag_re = re.compile('#\w+')

with open('geo_tweets_2013_04_15.mallet.txt', 'w') as fout:
    with open('/home/fryz/FirstResponder/MITLL_datasets/raw/geo_tweets_2013_04_14.csv', 'r') as f:
        r = csv.DictReader(f)
        for i,row in enumerate(r):

            print i,row
            raw_input('hit enter')
#
            #s = ''
            #for re_obj in hashtag_re.finditer(row['tweet_text']):
                #s += ' %s '%re_obj.group()
            #if len(s) > 0:
                #if 'iPhone' in row['source']:
                    #a = 'iPhone'
                #elif 'Android' in row['source']:
                    #a = 'Android'
                #elif 'BlackBerry' in row['source']:
                    #a = 'BlackBerry'
                #elif 'web' in row['source']:
                    #a = 'web'
                #else:
                    #a = 'various'
                #fout.write('%s %s %s\n'%(row['tweet_id'], a, s))
#
#
