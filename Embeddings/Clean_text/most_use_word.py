from nltk.book import *

def muw(text):

    bag = set(text)

    per = 0
    Word = ''

    Total = len(text)

    def percentage(count, total):
        return 100 * count / total

    for word in bag:
        if percentage(text.count(word), Total) >= per:
            per = percentage(text.count(word), Total)
            Word = word

    return {Word:per}

print(muw(text1))