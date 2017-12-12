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

################################################################################

rocket_synsets = wn.synsets('rocket')

for sense in rocket_synsets:
    lemmas = [l.name() for l in sense.lemmas()]
    print('Lemmas for sense : ' + sense.name() + ' ( ' + sense.definition() + ' ) - ' + str(lemmas))

# how it works?
print(rocket_synsets)
for i in rocket_synsets:
    print(i)
print(rocket_synsets[0])
print(rocket_synsets[0].definition())
print(rocket_synsets[0].lemmas())
print(rocket_synsets[0].lemmas()[0])
print(rocket_synsets[0].lemmas()[0].name())
print(rocket_synsets[0].lemmas()[1].name())



print(rocket_synsets[2])
print(rocket_synsets[2].definition())
print(rocket_synsets[2].lemmas())
print(rocket_synsets[2].lemmas()[4])
print(rocket_synsets[2].lemmas()[4].name())




################################################################################
ball_synsets = wn.synsets('ball')

# list of words that have one common meaning with one of the aceptinos of 'dog'
len(ball_synsets)

for i in ball_synsets:
    print(i)

# somethin pretty stupid and odvious
for i in ball_synsets:
    print(i, i.name())


for i in ball_synsets:
    print(i.name())
    print('---------')
    for j in i.lemmas():
        print(j)
    print('_________\n')


for i in ball_synsets:
    print(i)
    print('---------')
    print('DEFINITION: ')
    print(i.definition())
    print('---------')
    print(i.lemmas())
    print('=========\n')



################################################################################


# so, given a word in cannonical form, for example 'house'
# we can get a set of synonyms using:
house_synsets = wn.synsets('house')

# and for each one of this, we have a different meaning
print([j.definition() for j in house_synsets])

# and each one of this has its own unique 'name'
print([j.name() for j in house_synsets])

# and for each one of this, with its own name we can get access to its synonyms
print(wn.synset(house_synsets[0].name()))

# and more information: (using again the fact that it's a sysnset too)
print(wn.synset(house_synsets[0].name()).name())
print(wn.synset(house_synsets[0].name()).definition())

# now on lemmas: they are methods of the synset object
type(house_synsets[0])
print(house_synsets[0].lemmas())

# lemmas() gives us a list of the lemmas for this concrete synsets
print(house_synsets[0].lemmas()[0])

# it's a list of elemnts of the class lemma
type(house_synsets[0].lemmas()[0])

# This class has attributes, such as:
    # COUNT: The frequency of this lemma in wordnet
print(house_synsets[0].lemmas()[0].count())

    # SYNSET: synset
print(house_synsets[0].lemmas()[0].synset())

    # NAME: the cannonical name of this lemma
print(house_synsets[0].lemmas()[0].name())
