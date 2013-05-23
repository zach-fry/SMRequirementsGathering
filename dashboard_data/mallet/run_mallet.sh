cd /home/fryz/SMRequirementsGathering/dashboard_data/mallet

~/mallet-2.0.7/bin/mallet import-dir --input ./vectors \
                    --output ./hashtags.mallet \
                    --keep-sequence

~/mallet-2.0.7/bin/mallet train-topics --input ./hashtags.mallet \
                    --num-topics 20 \
                    --output-doc-topics ./output.txt \
                    --output-topic-keys ./keys.txt \
                    --optimize-interval 10
cd $OLDPWD
