from pydub import AudioSegment
from pydub.silence import split_on_silence

audiofile = AudioSegment.from_mp3("mailchimp.mp3")
audio_chunks = split_on_silence(audiofile, min_silence_len=50, silence_thresh=-19)
print len(audio_chunks)
for i, chunk in enumerate(audio_chunks):
	if i == 0:
		combined_sounds = chunk
	else:
		combined_sounds += chunk
	out_file = ".//splitAudio//chunk{0}.wav".format(i)
	print "exporting", out_file
	chunk.export(out_file, format="wav")

combined_sounds.export(".//splitAudio/finalChunk.wav", format = "wav")
