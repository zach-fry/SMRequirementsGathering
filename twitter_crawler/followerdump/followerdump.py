'''
@author Zach Fry (fryz)
@date 2/8/2013
'''

import os

#leave this
url = '"http://api.twittercounter.com/?apikey=e9335031a759f251ee9b4e2e6634e1c5&twitter_id='

#this changes to the directory that has the list of user ids in text files
follower_dir = '/home/fryz/twitter_crawler/followerdump/'
userfile = 'coems.txt'

#for userfile in os.listdir(follower_dir):
user_list = []
f = open(follower_dir+userfile, 'r')
for line in f:
    if line.strip() == '': pass
    if line.strip() in user_list: pass
    else: user_list.append(line.strip())
f.close()

data_dir = follower_dir + userfile[:len(userfile)-4]
if os.path.exists(data_dir) is False:
    os.mkdir(data_dir)

for user in user_list:
    #print url+user
    #raw_input()

    wget_cmd = 'wget -O %s/%s.tmp '%(data_dir,user)
    wget_cmd += url+user+'"'

    os.system(wget_cmd)
    os.system('python -mjson.tool < %s/%s.tmp > %s/%s.json'%(data_dir,user,data_dir,user))
    os.system('rm %s/%s.tmp'%(data_dir,user))
