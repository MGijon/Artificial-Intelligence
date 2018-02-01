from nltk.corpus import wordnet as wn

wn.synsets('think')
wn.synset('think.v.01').definition()

wn.synset('think.v.01').lemmas()

print(len(wn.synset('think.v.01').lemmas()))

for lemma in wn.synset('think.v.01').lemmas():
    print(lemma, lemma.frame_ids())
    print(' | '.join(lemma.frame_strings()))


type(wn.synset('think.v.01').lemmas())

type(wn.synset('think.v.01').lemmas()[0])

print(wn.synset('think.v.01').lemmas()[0].frame_ids())

type(wn.synset('think.v.01').lemmas()[0].frame_ids())

print(wn.synset('think.v.01').lemmas()[0].frame_strings())

type(wn.synset('think.v.01').lemmas()[0].frame_strings())

print(wn.synset('think.v.01').lemmas()[0].frame_strings()[0])
print(wn.synset('think.v.01').lemmas()[0].frame_strings()[1])
