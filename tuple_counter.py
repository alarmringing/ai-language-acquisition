
#INPUT: a list of integers, each number representing each k-means cluster assignmnet
def tuple_counter(segmentClusters):
	pairCount = Counter() #number of occurences for each pair of words
	for i in range(len(segmentClusters)-1):
		thisAssign = (segmentClusters[i], segmentClusters[i+1]) #this tuple
		pairCount[thisAssign] += 1 #count 

	#devide number of occurances by total number of occurances
	transProb = {k: v / (sum(pairCount.values())) for k, v in pairCount.items()} 
	return transProb
