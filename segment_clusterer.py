#from pydub import AudioSegment
import numpy, scipy, matplotlib.pyplot as plt, sklearn, librosa, mir_eval, urllib
from scipy.io.wavfile import write
import os 

#feature extractor
#def extract_features(x, fs):
#    zcr = librosa.zero_crossings(x).sum()
#    energy = scipy.linalg.norm(x)
#    return [zcr, energy]

#numpy.array
#looping through each segmented file
#for file in os.listdir("audio/output/self_recorded_files"):
#    if file.startswith("eechunk"):
        #print(file)
        #for each segmented file
#        x, fs = librosa.load("audio/output/self_recorded_files/" + file)


filename = 'audio/input/multisyllabic/multisyllabic_eric.wav'
x, fs = librosa.load(filename)

librosa.display.waveplot(x, fs)

onset_frames = librosa.onset.onset_detect(x, sr=fs, delta=0.15, wait=4)
onset_times = librosa.frames_to_time(onset_frames, sr=fs)

print onset_times
onset_samples = librosa.frames_to_samples(onset_frames)
librosa.output.times_csv('audio/output/multisyllabic_detection_eric_times.csv', onset_times)
x_with_beeps = mir_eval.sonify.clicks(onset_times, fs, length=len(x))
write("audio/output/multisyllabic_detection_eric.wav", fs, x+x_with_beeps)





#frame_sz = fs*0.090
#features = numpy.array([extract_features(x[i:i+frame_sz], fs) for i in onset_samples])
#print features.shape



def kmeans(vector, K, maxIters):
    '''
    list: list of examples, each example is a string-to-double dict representing a sparse vector.
    K: number of desired clusters. Assume that 0 < K <= |examples|.
    maxIters: maximum number of iterations to run for (you should terminate early if the algorithm converges).
    Return: (length K list of cluster centroids,
            list of assignments, (i.e. if examples[i] belongs to centers[j], then assignments[i] = j)
            final reconstruction loss)
    '''
    # BEGIN_YOUR_CODE (our solution is 32 lines of code, but don't worry if you deviate from this)
    random.seed(32)
    centroids = random.sample(vector, K) #these will be the initial random centroids 
    centroidsNormSqr = [0 for i in range(K)] #normSqr of each centroid (memoed)
    examplesNormSqr = [0 for i in range(len(examples))] #normSqr of each examples (memoed)
    assignments = [0 for i in range(len(examples))]
    finalLoss = 0

    #calculate norm squared values for each examples
    for i in range(len(examples)):
        examplesNormSqr[i] = dotProduct(examples[i],examples[i])

    for i in range(maxIters): 
        for k in range(K): #compute normSqr
            centroidsNormSqr[k] = dotProduct(centroids[k], centroids[k])
        finalLoss = 0
        groupCount = [0 for k in range(K)]
        #assign each data to centroid
        for j in range(len(examples)): 
            minDist = float('inf')
            minK = 0
            for k in range(K):
                thisDist = centroidsNormSqr[k] + examplesNormSqr[j] - 2*dotProduct(centroids[k], examples[j])
                if minDist > thisDist:
                    minDist = thisDist 
                    minK = k
            finalLoss += minDist 
            assignments[j] = minK
            groupCount[minK] += 1

        #update centroids 
        newCentroids = [dict() for k in range(K)]
        for j in range(len(assignments)):
            thisGroupNum = assignments[j]
            increment(newCentroids[thisGroupNum], 1/float(groupCount[thisGroupNum]), examples[j])

        #Check for early convergence
        if newCentroids == centroids: 
            break
        else: 
            centroids = newCentroids

    return (centroids, assignments, finalLoss)
