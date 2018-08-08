import pickle
from numpy import mean
from collections import Counter
import spacy 

with open('recipe.pkl','rb') as f:
	recipes = pickle.load(f)
print(mean([len(recipe['ingredients']) for recipe in recipes]))


nlp = spacy.load('en')
titles = [recipe['title'] for recipe in recipes]
words = []
for title in titles:
	doc = nlp(title)
	words += [token.text for token in doc if token.is_stop != True and token.is_punct != True]
count = Counter(words)

lstcount = list(count)
f = open('mostUsed.txt' ,'w')
for word in lstcount:
    f.write(word + '\n')
f.close()
