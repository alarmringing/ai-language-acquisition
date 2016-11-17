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