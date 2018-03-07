from textblob import TextBlob

# let's create our first textblob
Poe_Raven = Textblob('Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore')


## SENTIMENT ANALYSIS:
## ==================

# The 'sentiment' property returns a namedtuple of the form 'Sentiment(polarity, subjetivity)'
# , where polarity score is a float in range [-1.0, +1.0] and
# the subjetivity score is a float in range [0, +1.0] where 0 is very objetive and 1.0 subjetive.

print(Poe_Raven.sentiment)
print(Poe_Raven.sentiment.polarity)
print(Poe_Raven.sentiment.subjetivity)

## TOKENIZATION:
## ============

print(Poe_Raven.words)

print(Poe_Raven.sentences)







# source : http://textblob.readthedocs.io/en/dev/quickstart.html#create-a-textblob
