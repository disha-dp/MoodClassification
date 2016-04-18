def main():
	keyLines = open('keyoutput.txt','r').read().splitlines()
	nbLines = open('nboutput.txt', 'r').read().splitlines()
	with open('finalResults.txt', 'w') as fileOut:
		corrCount = 0
		for keyLine in keyLines:
			for nbLine in nbLines:
				if(keyLine == nbLine):
					fileOut.write("Correct\n")
					corrCount = corrCount+1
				else:
					fileOut.write("False\n")

		totalCount = len(nbLines)
		fileOut.write("FinalScore: %d" % corrCount)
		fileOut.write("/%d" % totalCount)
		#fileOut.write("Final Score: " + corrCount + "/" + totalCount)
		fileOut.close()
	return 

if __name__ == "__main__":
	main()