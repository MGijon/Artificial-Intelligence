# load text
filename = 'Kafka.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

# spliced by whitespace
spaced_words = text.split()
print(spaced_words[:100])

# select just words
import re
just_words = re.split(r'\W+', text)
print(just_words[:100])

# by whitespace and remove punctation; conserve contractions together
import string
print(string.punctuation)
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in spaced_words]
print(stripped[:100])

# if we want to normalize:
normalized_words = [word.lower() for word in spaced_words]
print(normalized_words[:100])