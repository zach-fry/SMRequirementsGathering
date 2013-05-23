'''
@author Zach Fry (fryz)
@date 2/13/2013
'''

import os
import codecs
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import to_tree
from scipy.spatial.distance import pdist
import numpy as np
import math

num_clusters = 25
dir_to_feature_vectors = '/home/fryz/hashtag_vectors/'

def loadFeatureVectors(path, feature_vectors, vocab_map):
    index = 0
    print 'Loading feature vectors'
    for vector_filename in os.listdir(path):
        fname = path + vector_filename
        f = codecs.open(fname, 'r', 'utf8')
        feature_vector = {}
        for line in f:
            word, freq = line.strip().split('\t')
            if word not in vocab_map:
                vocab_map[word] = index
                index += 1
            feature_vector[word] = int(freq)
        f.close()
    
        feature_vectors.append(feature_vector)

    #print 'There are %s feature vectors'%len(feature_vectors)
    #print 'There are %s words in vocab'%len(vocab_map.keys())

def calcTFIDF(feature_vectors, tf_idf_vectors):
    num_docs = len(feature_vectors)

    word_occurence = {}
    for feature_vector in feature_vectors:
        for word,freq in feature_vector.iteritems(): 
            if word in word_occurence:
                word_occurence[word] += 1
            else:
                word_occurence[word] = 1

    for feature_vector in feature_vectors:
        max_term = max(feature_vector.values())
        tf_idf_vector = []
        for word,freq in feature_vector.iteritems():
            tfidf = float(freq)/float(max_term)
            tfidf *= math.log(float(num_docs)/float(word_occurence[word]))
            tf_idf_vector.append((word, tfidf))


        tf_idf_vector = sorted(tf_idf_vector)
        tf_idf_vectors.append(tf_idf_vector)

        #print feature_vector
        #print tfidf_vector
        #raw_input()

#Clusters is a list of cluster nodes that has length num_clusters 
#each cluster node has a left, right, dist, id and count attribute
#cluster map maps cluster ids with cluster nodes
def initClusters(feature_vectors, vocab_map):
    print 'Initializing Clusters' 
    X = np.zeros( (len(feature_vectors), len(vocab_map.keys())) )
    for index,feature_vector in enumerate(feature_vectors):
        for word,freq in feature_vector:
            X.itemset((index, vocab_map[word]), freq)
    
    print 'Getting condensed distance matrix'
    Q = pdist(X, metric='cosine') 
    Q2 = map(lambda x: float(x+1)/float(2), Q)
    
    #print [ i for x,i in enumerate(Q) if x<0 ] 
    #raw_input()

    print 'Performing heirarchical clustering'
    Z = linkage(Q2, method='average', metric='cosine')
    root_cluster, cluster_map = to_tree(Z, rd=True)

    print 'Done Clustering'

    clusters = [ root_cluster ]
    while len(clusters) < num_clusters:
        cluster = clusters.pop()
        if cluster.left is None and cluster.right is None:
            print 'Error with clustering'
            raw_input()
        if cluster.left is not None:
            clusters.append(cluster.left)
        if cluster.right is not None:
            clusters.append(cluster.right)
        
        clusters = sorted(clusters, key=lambda x: x.dist)

    for cluster in clusters:
        print 'Cluster %s has %s docs'%(cluster.get_id(), cluster.get_count())

feature_vectors = []
vocab_map = {}
tf_idf_vectors = []

loadFeatureVectors(dir_to_feature_vectors, feature_vectors, vocab_map)
calcTFIDF(feature_vectors, tf_idf_vectors)
initClusters(tf_idf_vectors, vocab_map)

