//static demo
//old work
	//web_visuals
	//twitter_crawler
		*the API support will end soon
		*see more https://dev.twitter.com/docs/api/1/get/search
		//pastCrawler.py
			crawler made for boston bombing
		//crawler.py @data 2/10/2013
		
	//tweet_parser
	//topics 
		//greedy.py @date 2/14/2013
		//vectorize_hashtags.py @date 4/28/2013
			function loadTweets loads tweets(results of crawler), convert tweets to json format & creates tweet_dict
			function writeVectorsToFile writes tweets in tweet_dict to corresponding .txt file
			function getStopWords adds to the stopwords any hashtags found in > 25% of all tweets and occur <= 3 times in all tweets
		//plsa.py @date 2/13/2013
			function loadFeatureVectors
				for every vector files in /home/fryz/hashtag_vectors/, read them in
				for every line in every vector files, each line are word + freq
				fills each word + freq in feature_vectors dictionary. key = word, value = freq
				if the word is not in vocab_map dictionary, fill the word in vocab_map, value being the index of the word during the whole process			
			function calcTFIDF
			function initClusters
				Clusters is a list of cluster nodes that has length num_clusters each cluster node has a left, right, dist, id and count attribute cluster map maps cluster ids with cluster nodes
	//paper_tools
//dashboard_data
