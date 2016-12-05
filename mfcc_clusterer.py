#from pydub import AudioSegment
import numpy, scipy, matplotlib.pyplot as plt, sklearn, librosa, mir_eval, urllib
from scipy.io.wavfile import write
from scipy import sparse
from scikits.talkbox.features import mfcc
import os,sys

#feature extractor
def extract_features(x):
    ceps, mspec, spec = mfcc(x)
    num_ceps = len(ceps)
    X = []
    X.append(numpy.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0))
    Vx = numpy.array(X)
    return Vx


#These parameters are for testing.
#inputpath should be audio/output/self_recorded_files
#inputpathname should be eechunk
#outputpath should be audio/clustered/self_recorded_files
#outputpathname would be eecluster

def clusterAudioSegments( syllables, outputPath, outputFileName, fs, k):

    features = numpy.empty((0, 13))
    segments = list()
    #looping through each segmented file
    for syllable in syllables:
        feature = extract_features(syllable)
        features = numpy.vstack((features, feature))
        segments.append(syllable)

    #scale features from -1 to 1
    min_max_scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(-1, 1))
    features_scaled = min_max_scaler.fit_transform(features)

    #PyPlot this
    #plt.scatter(features_scaled[:,0], features_scaled[:,1])
    #plt.xlabel('Zero Crossing Rate (scaled)')
    #plt.ylabel('Spectral Centroid (scaled)')
    #plt.show()

    #kmeans 
    model = sklearn.cluster.KMeans(n_clusters = k)
    kmeansLabels = model.fit_predict(features_scaled)

    '''
    #affinity propogation
    model = sklearn.cluster.AffinityPropagation()
    apLabels = model.fit_predict(features_scaled)
    print ("Affinity propogation result: ", apLabels)
    '''

    #combine files in cluster
    results = [list() for _ in range(k)]
    padding = 30000; #padding within breaks
    for i in range(features.shape[0]):
        segment_to_attach = numpy.hstack(([0 for _ in range(padding)], segments[i]))
        results[kmeansLabels[i]] = numpy.hstack((results[kmeansLabels[i]], segment_to_attach))

    for i in range(k):
        out_file = outputPath + "/" + outputFileName + str(i) + ".wav"
        write(out_file, fs, results[i])

    return kmeansLabels


####################
#SCRIPT STARTS HERE#
####################

#clusterAudioSegments("audio/output/self_recorded_files", "kkchunk", "audio/clustered/self_recorded_files", "kkcluster", 4)
#clusterAudioSegments("audio/input/self_recorded_syllables", "ee", "audio/clustered/syllables", "eecluster", 4)
