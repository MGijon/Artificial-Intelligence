from nltk.book import *

## Counting Vocabulary;
## ====================

print('Moby Dick by Herman Melville (1851) has exactly ' + str(len(text1)) + ' words\n')

print('Moby Dick by Herman Melville (1851) has exactly ' + str(len(set(text1))) + ' diffent words')

print('Its lexical richness is ' + str( len(set(text1)) / len(text1)))

print('"he" is said ' + str(text1.count('he')) + ' times')

# it may be useful to define the next functions:
def lexical_diversity(text):
    return len(set(text))/len(text)

def percentage(count, total):
    return 100 * count / total

print('The lexical richness is again ' + str(lexical_diversity(text1)))

print('The percentage of times that "he" appears in the text is ' + str(percentage(text1.count('he'), len(text1))))