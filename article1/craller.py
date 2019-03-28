import switch as s
import json
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import re
import nltk
import pickle
from nltk.corpus import stopwords



def classify(text):
        documents=[]
        stemmer = WordNetLemmatizer()
        for sen in range(0, len(text)):
            # Remove all the special characters
            document = re.sub(r'\W', ' ', str(text[sen]))

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

            # Lemmatization
            document = document.split()

            document = [stemmer.lemmatize(word) for word in document]
            document = ' '.join(document)
            documents.append(document)




        with open('vectr', 'rb') as pic:
            vector=pickle.load(pic)
            text1=vector.fit_transform(documents).toarray()
        with open('tfidf', 'rb') as t:
            tfidfconverter = pickle.load(t)
            text2 = tfidfconverter.fit_transform(text1).toarray()

        with open('text_classifier', 'rb') as training_model:
            model = pickle.load(training_model)
            y_pred = model.predict(text2)
        return y_pred
