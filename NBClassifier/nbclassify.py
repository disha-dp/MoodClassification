import math
import sys
import os,glob
import array
import string
import numpy
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
allCategories = [0, 1, 2, 3, 4, 5, 6, 7] #SAD, HAPPY, ROMANTIC, PATRIOTIC, DEVOTIONAL, FUNNY, FRIENDSHIP, ANGRY
categoryNames = ['SAD', 'HAPPY', 'ROMANTIC', 'PATRIOTIC', 'DEVOTIONAL', 'FUNNY', 'FRIENDSHIP', 'ANGRY']

#create class list from the input 
score=[0, 0, 0, 0, 0, 0, 0, 0]
list_result={}
resultsFile = open('nboutput.txt','w')

def ApplyMultinomialNB(category, wordDictionary, prior, condProbability, document):
	global wordsInClass
	#print "test"
	#for doc in glob.glob(document + '/**/**/**/*.txt'):#, recursive=True
		#print "hello"
	if(1):
		try:
			newFile1=open(os.path.abspath(document),"r")
			words = [word for line in newFile1 for word in line.split()]				
			for category in allCategories:
				#print Decimal(prior[category])
				test = Decimal(prior[category])
				if(test == 0):
					test = 0.01
				score[category] = math.log10(Decimal(test))
				for word in words:
					wordToken = word.translate(string.maketrans("",""), string.punctuation).lower()
					if wordToken  in condProbability:#.keys():
						score[category] += math.log10(condProbability[wordToken][category])
		finally:
			newFile1.close()
		ranks=[0, 0, 0, 0, 0, 0, 0, 0]
		
		#maxIndices = np.argmax (score, axis=0)
		#DOES NOT KEEP TRACK OF MULTIPLE TAGS
		maxScore = 0;
		maxIndex = 0;
		for idx, val in enumerate(score):
			if val > maxScore:
				maxIndex = idx

		resultsFile.write(document + ' has tag of ' + categoryNames[maxIndex])
		# REMEMBER TO FIX
		#resultsFile.write(maxIndices[0] + 'TESTER TEST ' + doc + "\n")
		#if(len(maxIndices) =  )
		'''
		if score[2]>score[3] and score[0]>score[1]:
			res_file.write('truthful negative '+doc+"\n")
		else:
			if score[3]>score[2] and score[0]>score[1]:
				res_file.write('deceptive negative '+doc+"\n")
			else:
				if score[2]>score[3] and score[1]>score[0]:
					res_file.write('truthful positive '+doc+"\n")		
				else:
					res_file.write('deceptive positive '+doc+"\n")
		'''


	return # return class with max score


def main():
	wrong = 0
	with open('nbmodel.txt') as f:
	    wordDictionary, prior, condProbability = pickle.load(f)
	if len(sys.argv)>1:
		ApplyMultinomialNB(allCategories, wordDictionary, prior, condProbability, sys.argv[1])#last arg is the doc to classify
	#print "hi"
	return 

if __name__ == "__main__":
    main()
