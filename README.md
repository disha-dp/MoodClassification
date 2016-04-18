# MoodClassification
##Requirements
Code is written in Python (2.7) and requires Theano (0.7).
'polyglot-hi.pkl' is the file which has the maximum hindi words, in which each word is represented a 1x64 vector
##Data Collection
We used a selenium script to crawl webpages to get few thousand lyrics in Hindi.After getting the lyrics,they have to be manually tagged with an appropriate mood(Ex:Sad,Happy,Devotional etc)
##Data Preprocessing
To process the raw data use Preprocessingcode.py which takes Taggedsongs.txt as input.
This will create a pickle object mr.p,which has the data in the required format(vocabulary of all lyrics,word to index map for each word and the vector representation of each word)
##Training
