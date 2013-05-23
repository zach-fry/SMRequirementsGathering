from generateVisuals import *

hash_list = []
user_list = []
hash_counts = {}
hash_link_counts = {}
user_tag_map = {}

'''
These functions load information into the data structures above
'''
loadHashtagList('input/hashtag_list.txt', hash_list)
loadUserList('input/user_list.txt', user_list)
loadHashtagCounts('input/results/', hash_counts, hash_link_counts) 
loadUserTagMap('input/results/', user_tag_map, hash_list, user_list)

'''
These functions write the data structures into various formats used for these visualizations
'''
writeCSV(user_tag_map, 'output/')
writeHashtagWordCloudJSON(hash_counts, outpath='output/')
writeUserWordCloudJSON(user_tag_map, outpath='output/')
writeSymmetricCoOccurenceJSON(hash_link_counts, outpath='output/')
writeAsymmetricCoOccurenceJSON(user_tag_map, hash_list, user_list, outpath='output/')




