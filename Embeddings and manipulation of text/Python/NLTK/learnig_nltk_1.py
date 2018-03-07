from nltk.book import *

## Searching Text;
## ===============

text6.concordance('Ni')

print('=====================')

text6.similar('Hello')

print('=====================')

text6.common_contexts('Ni', 'Fence')

print('=====================')

# doing this way, by the way it's implemented in the class text, there's no way to
# change parameters in the graphic
# see : http://www.nltk.org/_modules/nltk/text.html
text6.dispersion_plot(['Ni', 'freedom'])

print('=====================')

# generating random text in the style of text 3
text6.generate()