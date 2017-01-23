# Modeling Infant Statistical Learning in Lexical Acquisition through Machine Learning
### Jihee Hwang (jiheeh), Krishan Kumar (krishank),  Eric Ehizokhale (eokhale)

This project aims to model the statistical lexical learnining that seems to occur in infants, who are able to figure out the lexical and phonological structure of a given language simply by listening to a continuous audio stream of it. 

* command: 
  ```javascript
  python pipeline.py
  ```

Run the above command, which will take care of all steps from reading the file to generating candidate words instance.
pipeline.py is structured as follows: 

* Detect syllables
 	```python
	create_syllables.create_syllables(inputDir, inputPathName)
    ```

* Splice audio by syllable
	```python
	splice_audio.splice_audio(inputDir, inputPathName, onset_times)
    ```

* Cluster syllables
	```python
	mfcc_clusterer.clusterAudioSegments(syllables, "audio/clustered/syllables", inputPathName, 22050, 12)
    ```

* Create dictionary of costs, a.e. how often each syllable combination occurs
	```python
	dictionary_builder.dictionary_builder(labelsTuple, 4)
    ```

* Run ucs based on the cost dictionary above, segment audio into appropriate parts
	```python
	ucs_word_segmenter.segmentWord(labelsTuple, cost_dictionary, 4)
	```

* Use ucs action data to re-build the final lexicon
	```python
	build_final_lexicon.build_final_lexicon(word_sequence)
	```

To change the input file, change the following parameters in pipeline.py: 

```python
inputDir = 'audio/input/sample'
inputPathName = 'sampleAudioGroup'
```


* optional functionality: 
	```python
	python sentence_generator.py
    ```

 Given an input lexicon, input_lexicon.txt, generate permutations of those words so that it's easier to create a self-recorded file from it. 
