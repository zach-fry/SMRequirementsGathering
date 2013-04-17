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

def requestURL(url, path, page):
    #print url
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        #print response.read()
    except Exception as e:
        f = open('error.txt', 'a')
        f.write('%s-%s\t%s\n'%(datestr,timestr,url))
        f.close()
        print type(e), e.args, e
    else:
        json_obj = json.loads(response.read())

        json_obj['date'] = datestr
        json_obj['time'] = timestr

        try:
            next_url = json_obj['next_page']
            return requestURL(root_url+next_url, path, page+1)
        except KeyError:
            return page
        finally:
            if len(json_obj['results']) > 0:
                f = open(path+'%s-%s-%s.json'%(datestr,timestr,page),'w')
                json.dump(json_obj, f, indent=4)
                f.close()
            else: pass

        f = open(path+'maxid.txt', 'w')
        f.write(str(json_obj['max_id']))
        f.close()
    
    return -1

def main():
    day = 'Boston/'
    global root_path
    root_path = root_path + day


    max_pages = {}
    for day in range(14,18):
        for tag in hashtags:
            if tag not in max_pages: max_pages[tag] = 1
            print 'extracting hashtag %s'%tag
            path = root_path + tag.strip('#')+'/'
            if os.path.isdir(path) is False or os.path.exists(path) is False:
                os.mkdir(path)

            stripped_tag = '%23' + tag.strip('#')
            url = root_url
            url += '?result_type=recent&lang=en&rpp=100&include_entities=true&until=2013-04-%s&q='%day
            url += stripped_tag

            page = max_pages[tag]
            while 1:
                tmp_url = url
                try:
                    f = open(path+'maxid.txt', 'r')
                    max_id = f.readline().strip()
                    f.close()
                    tmp_url += '&since_id=%s'%(max_id)
                except:
                    pass

                p = requestURL(tmp_url, path, max_pages[tag]) 
                if p > 0: break
                else: max_pages[tag] = p+1

main()

