# MoodClassification
##Requirements
Code is written in Python (2.7) and requires Theano (0.7).
'polyglot-hi.pkl' is the file which has the maximum hindi words, in which each word is represented a 1x64 vector
##Data Collection
We used a selenium script to crawl webpages to get few thousand lyrics in Hindi.After getting the lyrics,they have to be manually tagged with an appropriate mood(Ex:Sad,Happy,Devotional etc)
##Data Preprocessing
To process the raw data use Preprocessingcode.py which takes Taggedsongs.txt as input where lyric of each song is tagged with relavant mood.The data is split into 10 folds based on a CV value.
This will create a pickle object mr.p,which has the data in the required format(vocabulary of all lyrics,word to index map for each word and the vector representation of each word)
##Training and testing
The mr.p generated in the previous state will be taken as input,for each of the fold value,the data associated with that fold value is considered for training and the remaning folds will be taken as the test set and the input is trained using 3 different filter sizes and types.For each fold Performance will be displayed.The output will be the mean of the performance values.
