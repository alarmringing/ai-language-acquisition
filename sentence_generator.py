import itertools

#Given a set of input words, generates sentecnes 

with open('input_lexicon.txt') as f:
    input_lexicon = f.read().splitlines()
outfile = open('sentences_to_read.txt', 'w')

sentences_to_read = itertools.permutations(input_lexicon)
for sentence in sentences_to_read:

  outfile.write("%s\n" % ' '.join(sentence))


#print sentences_to_read
