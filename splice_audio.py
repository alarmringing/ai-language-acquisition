==from pydub import AudioSegment

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


times = get_times("audio/output/multisyllabic_detection_eric_times.csv")
print times
syllables = splice('audio/input/multisyllabic/multisyllabic_eric.wav', times)
for i, syllable in enumerate (syllables):
	out_file = ".//audio//output//syllables//eric_syllable{0}.wav".format(i)
	print "exporting", out_file
	syllable.export(out_file, format="wav")

#return syllables as vector
return syllables




