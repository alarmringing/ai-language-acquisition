#this scripts run every step that's required, given input audio
import create_syllables
import mfcc_clusterer
import splice_audio
import tuple_counter
import word_segmenter 

inputPath = 'audio/input/multisyllabic'
inputFileName = 'multisyllabic_english_2'

create_syllables.create_syllables(inputPath, inputFileName)
syllables = splice_audio.splice_audio(inputPath, inputFileName)
labels = mfcc_clusterer.clusterAudioSegments(syllables, "audio/clustered/syllables", "compcluster", 22050, 100) #k number is arbitrary for now
transProb = tuple_counter.tuple_counter(labels)
words = word_segmenter.word_segmenter(syllables, labels, transProb, 0.1)
wordClusters = mfcc_clusterer.clusterAudioSegments(words, "audio/clustered/words", "compcluster", 22050, 50)

