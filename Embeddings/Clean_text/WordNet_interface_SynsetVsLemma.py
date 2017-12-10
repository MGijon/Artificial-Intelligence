from nltk.corpus import wordnet as wn

'''
SYNSET VS LEMMA:
===============
The terms are based on the general sense of the words "lemma" and "synonym".

A lemma is wordnet's version of an entry in a dictionary: A word in canonical form,
with a single meaning. E.g., if you wanted to look up "banks" in the dictionary,
the canonical form would be "bank" and there would be separate lemmas for the
nouns meaning "financial institution" and "side of the river", a separate one
for the verb "to bank (on)", etc.

The term synset stands for "set of synonyms". A set of synonyms is a set of words
with similar meaning, , e.g. ship, skiff, canoe, kayak might all be synonyms for
boat. In the nltk, a synset is in fact a set of lemmas with related meaning.
'''

cake_synsets = wn.synsets('cake')

for sense in cake_synsets:
    lemmas =  [l.name() for l in sense.lemmas()]
    print('Lemmas for sense : ' + sense.name() + ' ( ' + sense.definition() + ' ) - ' + str(lemmas))













# source : http://justanoderbit.blogspot.com.es/2017/10/synset-vs-lemma.html
