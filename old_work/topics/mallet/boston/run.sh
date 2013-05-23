~/mallet-2.0.7/bin/mallet import-file --input geo_tweets_2013_04_15.mallet.txt \
                    --output geo_tweets_2013_04_15.mallet \
                    --remove-stopwords \
                    --keep-sequence

~/mallet-2.0.7/bin/mallet train-topics --input geo_tweets_2013_04_15.mallet \
                    --num-topics 50 \
                    --output-doc-topics output.txt \
                    --output-topic-keys keys.txt \
                    --optimize-interval 10
