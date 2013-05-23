import urllib
import urllib2
import StringIO
import csv
import re
import codecs
import time
import datetime
import subprocess
import os
import math
import operator
import json

'''
GLOBALS
'''
hashtag_re = re.compile('#\w\w+')
tweet_vector_dir = 'mallet/vectors'
timestamps = {}
user_tag_dict = {}

'''
Get the results from the endpoint
'''
endpoint = "http://firstresponders.tw.rpi.edu/sparql2"
query = " select distinct ?status ?message ?user ?timestamp where { \
    graph ?g { \
    ?status <http://www.w3.org/ns/prov#wasAttributedTo> ?user; \
            <http://www.w3.org/ns/prov#value> ?message; \
            <http://purl.org/dc/terms/subject> ?hashtag; \
            <http://purl.org/dc/terms/date> ?timestamp \
        } \
    } limit 1000" 

params = {'output' : 'csv', 'query': query}

data = urllib.urlencode(params)
req = urllib2.Request(endpoint, data)
response = urllib2.urlopen(req)

'''
Read the CSV output from the endpoint
'''
f = StringIO.StringIO(response.read())
reader = csv.DictReader(f)
for row in reader:
    id = row['status'].split('/')[-1]

    #vectorize the hashtags
    hashtags = []
    if hashtag_re.search(row['message']) is not None:
        fout = codecs.open('%s/%s.txt'%(tweet_vector_dir,id), 'w', 'utf8')
        for each in hashtag_re.finditer(row['message']):
            hashtags.append(each.group())
            fout.write('%s\n'%each.group())
        fout.close()
    hashtags = list(set(hashtags))

    #get timestamps 
    raw_timestamp = str(time.mktime(datetime.datetime.strptime(row['timestamp'], "%Y-%m-%dT%H:%M:%SZ").timetuple()))
    timestamp = raw_timestamp[:len(raw_timestamp)-2]+'000'
    if timestamp not in timestamps: timestamps[timestamp] = 0
    timestamps[timestamp] += 1

    #populate the user_tag_dict
    if row['user'] not in user_tag_dict: user_tag_dict[row['user']] = {}
    for tag in hashtags:
        if tag not in user_tag_dict[row['user']]: user_tag_dict[row['user']][tag] = 0
        user_tag_dict[row['user']][tag] += 1
    
'''
Write out the timestamps file for the static demo
'''
f = open('output/timestamps.js', 'w')
f.write('var times=[')
n = len(timestamps)-1
i = 0;
for k,v in timestamps.iteritems():
    if i == n: f.write('[%s,%s]];\n'%(k,v))
    else: 
        f.write('[%s,%s],'%(k,v))
        i += 1
f.close()

'''
Write out mallet output to static demo
'''
try:
    with open(os.devnull, 'wb') as shutup:
        r = subprocess.check_call(["/bin/sh", "mallet/run_mallet.sh"], stdout=shutup, stderr=shutup)

    f_topics = open('mallet/keys.txt', 'r')
    topics = f_topics.readlines()
    f_topics.close()

    f_output = open('output/mallet_output_wrapper.txt', 'w')
    f_output.write('var output = "')
    n = len(topics)-1
    i = 0
    for line in topics:
        if i == n: f_output.write('%s";\n'%line.strip())
        else:
            f_output.write('%s #\\\n'%line.strip())
            i += 1
        
    f_output.close()

except subprocess.CalledProcessError as e:
    print e
    print e.returncode

'''
Filter out the top 20 users by weighted entropy for a list of hashtags
    (# of times user mentioned all hashtags) * (log_2 [counted # of hashtags they used on the list])
Write out the co-occurence matrix file
'''
try:
    f = open('hashtag_list.txt', 'r')
    hashtags = map(lambda x: x.strip(), f.readlines())
    f.close()

    #do the scoring and filtering
    user_scores = {}
    for user,tag_freq in user_tag_dict.iteritems():
        total_count = sum([tag_freq[x] for x in tag_freq.keys() if x in hashtags])
        try:
            entropy = math.log(sum([1 for x in tag_freq.keys() if x in hashtags]), 2)
        except ValueError:
            entropy = 0
        score = float(total_count) * float(entropy)
        if score > 0:
            user_scores[user] = score

    sorted_scores = sorted(user_scores.iteritems(), key=operator.itemgetter(1), reverse=True)
    
    #write it out to the json file
    users = []
    d = {}
    d['users'] = []
    d['tags'] = []
    d['links'] = []
    for user,score in sorted_scores[:20]:
        d['users'].append({'group':1, 'name':'@'+user.split('/')[-1]})
        users.append(user)
    for tag in hashtags:
        d['tags'].append({'group':1, 'tag':tag})
    for user,tag_freq in user_tag_dict.iteritems():
        for tag, freq in tag_freq.iteritems():
            if tag in hashtags:
                try:
                    d['links'].append({'toTag':hashtags.index(tag), 'fromUser':users.index(user), 'value':freq} )
                except ValueError:
                    pass

    f = open('output/matrix_co_tag_user.json', 'w')
    json.dump(d, f)
    f.close()

except IOError:
    print 'Put the list of hashtags for the Co Occurence Matrix in hashtag_list.txt'
    print 'One hashtag with the #, per line seperated by newline'
