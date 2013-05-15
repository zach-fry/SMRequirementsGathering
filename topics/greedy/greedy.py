'''
@author Zach Fry (fryz)
@date 2/14/2013
'''

import os
import json
import codecs

tag_counts = {}
hashtag_dirs = '/home/fryz/twitter_crawler/results/'
for tag_dir in os.listdir(hashtag_dirs):
    tag_counts[tag_dir] = {}
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
                    if tag in tag_counts[tag_dir]:
                        tag_counts[tag_dir][tag] += 1
                    else:
                        tag_counts[tag_dir][tag] = 1
#
    #f = codecs.open('./counts/%s.txt'%tag_dir, 'w', 'utf8')
    #for k,v in tag_counts[tag_dir].iteritems():
        #f.write('%s\t%s\n'%(k,v))
    #f.close()


num_tags = 100
top_tags = []
f = codecs.open('/home/fryz/twitter_crawler/stats/hashtags.counts.sorted', 'r', 'utf8')
top_tags = map(lambda x: x.strip().split('\t')[0], f.readlines()[:num_tags])
f.close()

cluster_list = tag_counts.keys()
nodes_index_map = []
nodes = []
for top_tag in top_tags:
    max_count = 0
    cluster = -1
    if top_tag in cluster_list: 
        cluster = cluster_list.index(top_tag)
    else:
        for tag_name,tags in tag_counts.iteritems():
            if top_tag in tags:
                if tags[top_tag] > max_count:
                    max_count = tags[top_tag]
                    cluster = cluster_list.index(tag_name)
            else: pass

    if cluster == -1:
        print 'error'
        raw_input()
    else:
        node = {}
        node["name"] = top_tag
        node["group"] = cluster
        nodes.append(node)
        nodes_index_map.append(top_tag)

link_dict = {}
f = codecs.open('/home/fryz/twitter_crawler/stats/hashtags.links', 'r', 'utf8')
for line in f:
    tag1, tag2, freq = line.strip().split('\t')
    if tag1 in top_tags and tag2 in top_tags:
        link_dict[tag1] = {tag2 : freq}
f.close()

links = []
for i in range(len(top_tags)):
    for j in range(i,len(top_tags)):
        if top_tags[i] in link_dict:
            if top_tags[j] in link_dict[top_tags[i]]:
                link = {}
                link["source"] = nodes_index_map.index(top_tags[i])
                link["target"] = nodes_index_map.index(top_tags[j])
                link["value"] = link_dict[top_tags[i]][top_tags[j]]
                links.append(link)
        elif top_tags[j] in link_dict:
            if top_tags[i] in link_dict[top_tags[j]]:
                link = {}
                link["source"] = nodes_index_map.index(top_tags[j])
                link["target"] = nodes_index_map.index(top_tags[i])
                link["value"] = link_dict[top_tags[j]][top_tags[i]]
                links.append(link)
        else:
            pass

f = open('./graph.json', 'w')
g = {"nodes" : nodes , "links" : links}
json.dump(g, f)
f.close()

