from pydub import AudioSegment
import numpy, scipy, matplotlib.pyplot as plt, sklearn, librosa, mir_eval, urllib

def splice(audioFile, times):
	audio = AudioSegment.from_wav(audioFile)
	syllables = []
	for i in range(len(times)):
		t = times[i]
		t = t * 1000 #set to milliseconds, might have to drop sig figs
		if i == 0:
			syllables.append(audio[:t])
		else:
			t_prev = times[i - 1] * 1000
			syllables.append(audio[t_prev:t])
			print str(t_prev) + " " + str(t)

		if i == len(times) - 1:
			syllables.append(audio[t:])
	return syllables

def get_times(timeFile):
	times = []
	with open(timeFile) as f:
		for line in f:
			times.append(float(line.strip()))
	return times

def splice_audio(inputPath, inputFileName):
	times = get_times("audio/output/onset_detection/" + inputFileName + "_times.csv")
	print times
	syllables = splice(inputPath + '/' + inputFileName + '.wav', times)
	raw_syllables = list()
	for i, syllable in enumerate (syllables):
		out_file = "./audio/output/syllables/" + inputFileName + "/" + inputFileName + "{0}.wav".format(i)
		print "exporting", out_file
		syllable.export(out_file, format="wav")
		x, fs = librosa.load(out_file)
		raw_syllables.append(x)

	#return syllables as vector
	return raw_syllables

#audio/input/multisyllabic
#multisyllabic_eric




