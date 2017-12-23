from nltk.corpus import wordnet as wn

# choose one of the synsets of 'Dog'
Dog = wn.synsets('dog')[0]
Dog

# set of tuples (synset, int)
Hyper_Distances_Dog = Dog.hypernym_distances()
