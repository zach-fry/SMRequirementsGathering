~/mallet-2.0.7/bin/mallet import-dir --input ../../vectors \
                    --output hashtags.mallet \
                    --remove-stopwords \
                    --stoplist-file stopwords.txt \
                    --keep-sequence

~/mallet-2.0.7/bin/mallet train-topics --input hashtags.mallet \
                    --num-topics 10 \
                    --output-doc-topics output.txt \
                    --output-topic-keys keys.txt \
                    --optimize-interval 10
