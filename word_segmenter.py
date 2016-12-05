import numpy 

#INPUT: segmentClusters - a list of integers, each number representing each k-means cluster assignment, 
#	transProb - the map of syllable pairs and their associated transitional porbabilites, threshold - the threshold probability 
#RETURN: a list of audio vectors, each element is a word 
def word_segmenter(segments, segmentClusters, transProb, threshold):

	temp = numpy.empty([0,])
	words = list()
	for i in range (len(segmentClusters)-1):
		thisSegment = segments[i]
		temp = numpy.append(temp, thisSegment[:])
		thisKey = (segmentClusters[i], segmentClusters[i+1])
		if transProb[thisKey] > threshold: 
			continue
		else: 
			words.append(temp)
			temp = numpy.empty([0,0])

	print("Final count of words is ", len(words))
	return words 



	# for in in range of segmentClusters, add syllable i to the temp vector 
		# if transProb[(i, i+1)] > threshold: continue 
		# else,  add temp vector to final list, empty temp vector 

	# return the final list 

