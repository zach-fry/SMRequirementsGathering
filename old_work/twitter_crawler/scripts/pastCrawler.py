'''
@author Zach Fry (fryz)
@date 4/17/2013
'''

import os
from time import strftime, localtime
import json
import urllib2

hashtags = ['#SMEM',
            '#SMEMChat',
            '#EM',
            '#EGov',
            '#OGov',
            '#Gov20',
            '#HSEM',
            '#SM',
            '#WX',
            '#2BeeRdy',
            '#CoEMS',
            '#NEMA',
            '#IAEM',
            '#UASI',
            '#VSMWG',
            '#IAEMETC',
            '#firstresponder']

datestr = strftime('%m-%d-%Y', localtime())
timestr = strftime('%H:%M', localtime())
root_url = 'http://search.twitter.com/search.json'
root_path = '/home/fryz/FirstResponder/twitter_crawler/results/'

def requestURL(url):
    #print url
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        #print response.read()
    except Exception as e:
        #if isinstance(e, urllib2.HTTPError):
        f = open('error.txt', 'a')
        f.write('%s-%s\t%s\t%s\n'%(datestr,timestr,url,e))
        f.close()
        return None
        #print type(e), e.args, e
    else:
        return json.loads(response.read())

def parseTweets(json_obj, path):
        try:
            maxid = str(json_obj['max_id'])
            f = open(path+'maxid.txt', 'w')
            f.write('%s\n'%maxid)
            f.close()

            if len(json_obj['results']) > 0:
                index = 0
                if os.path.exists('%s.json'%maxid):
                    index = 1
                    while os.path.exists('%s-%s.json'%(maxid,index)): index += 1

                if index > 0:
                    f = open(path+'%s-%s.json'%(maxid, index),'w')
                else: 
                    f = open(path+'%s.json'%(maxid),'w')
                json.dump(json_obj, f, indent=4)
                f.close()
            else: pass
            
            next_url = root_url + json_obj['next_page']
            print next_url
            return next_url

        except KeyError:
            return None


def main():
    day = 'Boston/'
    global root_path
    root_path = root_path + day

    for day in range(14,20):
        for tag in hashtags:
            print 'extracting hashtag %s'%tag
            path = root_path + tag.strip('#')+'/'
            if os.path.isdir(path) is False or os.path.exists(path) is False:
                os.mkdir(path)

            stripped_tag = '%23' + tag.strip('#')
            url = root_url
            url += '?result_type=recent&lang=en&rpp=100&include_entities=true&until=2013-04-%s&q='%day
            url += stripped_tag

            while 1:
                tmp_url = url
                try:
                    f = open(path+'maxid.txt', 'r')
                    max_id = f.readline().strip()
                    f.close()
                    tmp_url += '&since_id=%s'%(max_id)
                except:
                    pass
                    
                json_object = requestURL(tmp_url)
                if json_object is None:
                    print 'Error processing request to %s'%tmp_url
                    break
                
                p = parseTweets(json_object, path)
                while p is not None:
                    json_object = requestURL(p)
                    if json_object is None: break
                    p = parseTweets(json_object, path)



main()

