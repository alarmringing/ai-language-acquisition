from pydub import AudioSegment
from pydub.silence import split_on_silence

audiofile = AudioSegment.from_mp3("audio/input/self_recorded_files/ee_self_recorded.mp3")
audio_chunks = split_on_silence(audiofile, min_silence_len=20, silence_thresh=-28)
print len(audio_chunks)
for i, chunk in enumerate(audio_chunks):
	if i == 0:
		combined_sounds = chunk
	else:
		combined_sounds += chunk
	out_file = ".//audio//output//self_recorded_files//eechunk{0}.wav".format(i)
	print "exporting", out_file
	chunk.export(out_file, format="wav")

combined_sounds.export(".//audio/output/self_recorded_files/eefinalChunk.wav", format = "wav")
