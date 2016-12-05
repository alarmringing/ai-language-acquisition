#this scripts run every step that's required, given input audio
import create_syllables
import mfcc_clusterer
import splice_audio
import tuple_counter
import word_segmenter 

inputPath = 'audio/input/multisyllabic'
inputFileName = 'multisyllabic_jihee_long'

create_syllables.create_syllables(inputPath, inputFileName)
syllables = splice_audio.splice_audio(inputPath, inputFileName)
labels = mfcc_clusterer.clusterAudioSegments(syllables, "audio/clustered/syllables", "multisyllabic_jihee_long_cluster", 22050, 12) #k number is arbitrary for now
transProb = tuple_counter.tuple_counter(labels)
#tweak constant so that word_segmenter should generate roughly 80 words
words = word_segmenter.word_segmenter(syllables, labels, transProb, 0.025)
wordClusters = mfcc_clusterer.clusterAudioSegments(words, "audio/clustered/words", "multisyllabic_jihee_long_cluster", 22050, 6)
