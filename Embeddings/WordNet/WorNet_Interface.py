from nltk.corpus import wordnet as wn

### SYNSET: a set of synonyms that share a common meaning
### ======
### =====================================================

wn.synsets('dog')

## The 'synsets' function has an optional argument that lests you constrain the part of
## speech of the word:
## ====================================================================================

# VERB
# ----
wn.synsets('dog', pos = wn.VERB)
wn.synsets('house', pos = wn.VERB)

# NOUN
# ----
wn.synsets('dog', pos = wn.NOUN)
wn.synsets('house', pos = wn.NOUN)

# ADJ
# ---
wn.synsets('dog', pos = wn.ADJ)
wn.synsets('house', pos = wn.ADJ)

# ADV
# ---
wn.synsets('dog', pos = wn.ADV)
wn.synsets('house', pos = wn.ADV)

## A synset is identified with a 3-part name of the form :
## WORD.POS.NN
## =======================================================

print(wn.synset('dog.n.01').definition())

print(wn.synset('dog.n.03').definition())


type(wn.synsets('dog'))
dog = wn.synsets('dog')
len(dog)

type(dog[1])

dog[0].definition()

dog[0].examples()
type(dog[0].examples())
len(dog[0].examples())

## LEMMA: represent a specifuc sense o a specific word
## =====
## ---------------------------------------------------

dog[0].lemmas()
type(dog[0].lemmas())
len(dog[0].lemmas())
for w in dog[0].lemmas():
    print(w)

wn.lemma('dog.n.01.dog')
wn.lemma('dog.n.01.dog').synset()

#######################################################

print(wn.synset('dog.n.02'.definition())) # doesn't exist

for i in wn.synsets('dog'):
    print(i)

print(wn.synset('frump.n.01').definition())
for i in wn.synsets('dog'):
    print(i.definition())
