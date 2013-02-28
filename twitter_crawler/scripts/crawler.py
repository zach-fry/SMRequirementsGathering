'''
@author Zach Fry (fryz)
@date 2/10/2013
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
root_path = '/home/fryz/twitter_crawler/results/'

def requestURL(url, path, page):
    #print url
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        #print response.read()
    except:
        f = open('error.txt', 'a')
        f.write('%s-%s\t%s\n'%(datestr,timestr,url))
        f.close()
    else:
        json_obj = json.loads(response.read())

        json_obj['date'] = datestr
        json_obj['time'] = timestr

        try:
            next_url = json_obj['next_page']
            requestURL(root_url+next_url, path, page+1)
        except KeyError:
           pass
        finally:
            if len(json_obj['results']) > 0:
                f = open(path+'%s-%s-%s.json'%(datestr,timestr,page),'w')
                json.dump(json_obj, f, indent=4)
                f.close()
            else: pass

        f = open(path+'maxid.txt', 'w')
        f.write(str(json_obj['max_id']))
        f.close()

def main():
    day = 'Feb21/'
    global root_path
    root_path = root_path + day

    for tag in hashtags:
        path = root_path + tag.strip('#')+'/'
        if os.path.isdir(path) is False or os.path.exists(path) is False:
            os.mkdir(path)

        stripped_tag = '%23' + tag.strip('#')
        url = root_url
        url += '?result_type=recent&rpp=100&lang=en&rpp=100&include_entities=true&q='
        url += stripped_tag

        try:
            f = open(path+'maxid.txt', 'r')
            max_id = f.readline().strip()
            f.close()
            url += '&since_id=%s'%(max_id)
        except:
            pass

        requestURL(url, path, 1)


main()
