import json
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import re
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
import pickle
from nltk.corpus import stopwords

label=[]
textt=[]
count11=0
count1=0

with open ('dataset.txt') as mm:

    for line in mm:
        m=json.loads(str(line))
        if m['category'] != 'POLITICS' and count1<20000:
            label.append('NPOLITICS')
            textt.append(m['headline'])
        elif m['category']=='POLITICS' and count11<40000:
            label.append('POLITICS')
            textt.append(m['headline'])



documents=[]
stemmer = WordNetLemmatizer()
for sen in range(0, len(textt)):
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(textt[sen]))
    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    # Removing prefixed 'b'
    document = re.sub(r'^b\s+', '', document)
    # Converting to Lowercase
    document = document.lower()
    # Lemmatizatio
    document = document.split()
    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)
    documents.append(document)


tfidfconverter = TfidfVectorizer(max_features=800, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
tfidfconverter.fit(documents)
X = tfidfconverter.transform(documents)

with open('tfid', 'wb') as picklefile1:
    pickle.dump(tfidfconverter,picklefile1)


X_train, X_test, y_train, y_test = train_test_split(X, label, test_size=0.2, random_state=0)
classifier = RandomForestClassifier(n_estimators=100, random_state=0)
classifier.fit(X_train, y_train)

with open('text_classifier', 'wb') as picklefile:
    pickle.dump(classifier,picklefile)

