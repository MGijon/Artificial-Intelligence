from nltk.corpus import wordnet as wn

# Check the definitions of the diferents synset of 'cat' until
# i found something to use.

wn.synsets('cat')

cat = wn.synset('cat.n.01')

cat.definition()


## HYPERNYMS: synsets that are more 'general'
## =========

cat.hypernyms()

cat.hypernym_distances()

cat.hypernym_paths()


## HYPONYMS: synsets that are more 'specific'
## ========

cat.hyponyms()

## MEMBER HOLONYMS: things that the item is contained in
## ===============

cat.member_holonyms()

## MEMBER MERONYMS: are components of substances that make up the item
## ===============

cat.member_meronyms()

cat.root_hypernyms()

cat.lowest_common_hypernyms(wn.synset('dog.n.01'))




################################################################################

wn.synsets('plant')
wn.synset('plant.n.02').definition()

plant = wn.synset('plant.n.02')

# More general
plant.hypernyms()

# More specific
plant.hyponyms()

# item contained in
plant.member_holonyms()

# components or substances of the item
plant.member_meronyms()

plant.root_hypernyms()

plant.lowest_common_hypernyms(wn.synset('dog.n.01'))




################################################################################

wn.synsets('car', pos = wn.NOUN)
wn.synset('car.n.01').definition()

car = wn.synset('car.n.01')

car.hypernyms()

car.hyponyms()

car.member_holonyms()

car.member_meronyms()




################################################################################

wn.synsets('men', pos = wn.NOUN)
wn.synset('man.n.03').definition()

man = wn.synset('man.n.03')

man.hypernyms()

man.hyponyms()

man.member_holonyms()

man.member_meronyms()




################################################################################

wn.synsets('cow', pos = wn.NOUN)

wn.synset('cow.n.01').definition()

cow = wn.synset('cow.n.01')

# more general
cow.hypernyms()

# more specific
cow.hyponyms()

# item contained in
cow.member_holonyms()

# components or substances of the item
cow.member_meronyms()




################################################################################
