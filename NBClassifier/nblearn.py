import math
import sys
import os,glob
import array
import string
from collections import Counter
from decimal import Decimal
import heapq
import pickle
'''
NEG = 0
POS = 1
TRUE = 2
DEC = 3
'''
SAD = 0
HAPPY = 1
ROMANTIC = 2
PATRIOTIC = 3
DEVOTIONAL = 4
FUNNY = 5
FRIENDSHIP = 6
ANGRY = 7
'''
#C is superset of category classes
C=[0,1,2,3]#"negative","positive","true","dec"]	
'''
allCategories = [0, 1, 2, 3, 4, 5, 6, 7] #SAD, HAPPY, ROMATNIC, PATRIOTIC, DEVOTIONAL, FUNNY, FRIENDSHIP, ANGRY

#create class list from the input 
totalNumberOfDocuments = 0
docsInClass = [0, 0, 0, 0, 0, 0, 0, 0]
wordsInClass = [0, 0, 0, 0, 0, 0, 0, 0] 
prior = [0, 0, 0, 0, 0, 0, 0, 0]
score = [0, 0, 0, 0, 0, 0, 0, 0]
wordDictionary = {}
condProbability = {}
listResult = {}

def readWords(category):
	#folds={'fold2','fold3','fold4'}
	#for fold in folds:
	#	os.chdir(fold)
		for doc in glob.glob("*.txt"):
			docsInClass[category]=docsInClass[category] + 1
			global totalNumberOfDocuments
			totalNumberOfDocuments = totalNumberOfDocuments + 1 #keep incrementing doc count
			try:
				newFile = open(doc,"r")
				words=[word for line in newFile for word in line.split()]				
				wordsInClass[category] = wordsInClass[category]+len(words)
				for word in words:
					#words = [word for line in newFile for word in line.split()]
					words = line.split(" ")				
					wordsInClass[category]=wordsInClass[category]+len(words)
					#WordsInClass[C2]=WordsInClass[C2]+len(words)
					for word in words:
						wordToken = word.translate(string.maketrans("",""), string.punctuation).lower()
						if wordToken not in wordDictionary.keys():
							wordDictionary[wordToken]=[0, 0, 0, 0, 0, 0, 0, 0]		#add (word:1 in class to which it belongs)
						wordDictionary[wordToken][category] = wordDictionary[wordToken][category] + 1
						#word_dict[word_token][C2]=word_dict[word_token][C2]+1
			finally:
				newFile.close()
	#os.chdir('../')
	#return

def ExtractVocab(dir):
	os.chdir(dir)

	#os.chdir("negative_polarity")
	os.chdir("SAD")
	readWords(SAD)
	
	os.chdir("../")
	os.chdir("HAPPY")
	readWords(HAPPY)
	
	os.chdir("../")
	os.chdir("ROMANTIC")
	readWords(ROMANTIC)

	os.chdir("../")
	#os.chdir("PATRIOTIC")
	readWords(PATRIOTIC)

'''
	os.chdir("../")
	#os.chdir("DEVOTIONAL")
	readWords(DEVOTIONAL)	

	os.chdir("../")
	#os.chdir("FUNNY")
	readWords(FUNNY)

	os.chdir("../")
	#os.chdir("FRIENDSHIP")
	readWords(FRIENDSHIP)
	
	os.chdir("../")
	#os.chdir("ANGRY")
	readWords(ANGRY)
'''

	#return

def printMap(diction):
	for word in diction:
		print word
		print diction[word]

def TrainMultinomialNB(dir):
	global condProbability
	ExtractVocab(dir)
	for category in allCategories: #say we are talking about class negative
		currentCategory = docsInClass[category]	#c should translate to an index in DocsInClass
		prior[category] = Decimal(currentCategory)/totalNumberOfDocuments
		#textc = wordsInClass[category] #ConcatenateTextOfAllDocsInClass(D,c)
		for word in wordDictionary:
			numberOfWordAppearancesInCategory = wordDictionary[word][category]	#count the number of times the word belonged to that class
								#CountTokesOfTerm(textc,t`)
			if word not in condProbability:#.keys():
				condProbability[word]=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
			condProbability[word][category] = (float(numberOfWordAppearancesInCategory)+1)/(wordsInClass[category]+len(wordDictionary)) 
	os.chdir("../")

	with open('nbmodel.txt', 'w') as f:
		pickle.dump([wordDictionary, prior, condProbability], f)
	f.close()
	return #word_dict,prior,condProb

def main():
	'''
	counting = 0
	for root, dirs, files in os.walk(os.getcwd()):
	    for fil in files:
	    	if fil.endswith(('.txt')):
			    print fil
	'''
	if len(sys.argv)>1:
		TrainMultinomialNB(sys.argv[1])
	else:
		print "There is no argument"

	print "Done"
	return 

if __name__ == "__main__":
    main()
