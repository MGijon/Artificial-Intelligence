from nltk.corpus import wordnet as wn

wn.synsets('cat')

cat = wn.synset('cat.n.01')

cat.definition()

cat.hypernyms()

cat.hypernym_distances()

cat.hypernym_paths()

cat.hyponyms()

cat.member_holonyms()

cat.member_meronyms()

cat.root_hypernyms()

cat.lowest_common_hypernyms(wn.synset('dog.n.01'))
