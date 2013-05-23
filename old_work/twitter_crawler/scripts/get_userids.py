import os
import json

userids = []
for fp in os.listdir('.'):
    try:
        f = open('./%s'%fp, 'r')
        jobj = json.load(f)
        f.close()
        for r in jobj['results']:
            userids.append(r['id'])
    except:
        print fp

f = open('./userids.txt', 'w')
for ids in userids:
    f.write('%s\n'%ids)
f.close()
