import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

class ThematicAnalysis:
    def __init__(self):
        pass

    def preprocess_text(self, text):
        """
        Preprocess the text by tokenizing and converting to lowercase.
        
        :param text: String of text to preprocess.
        :return: List of tokens.
        """
        tokens = word_tokenize(text.lower())
        lemmatizer = WordNetLemmatizer()
        stop_words = set(stopwords.words('english'))
        tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]
        return ' '.join(tokens)
    
    def get_keyword(self, text, n=100):
        """
        Extract keywords from the text using TF-IDF.
        """

        # Initialize TF-IDF Vectorizer
        # min_df: ignore terms that appear in less than 2 documents
        # max_df: ignore terms that appear in more than 90% of documents
        # ngram_range: consider unigrams and bigrams
        tfidf_vectorizer = TfidfVectorizer(min_df=2, max_df=0.90, ngram_range=(1, 2))

        # Fit and transform the cleaned reviews
        tfidf_matrix = tfidf_vectorizer.fit_transform(text)

        # Get feature names (the words and n-grams)
        feature_names = tfidf_vectorizer.get_feature_names_out()

        # Display top N terms/phrases
        print(f"\nTop {n} common terms/phrases:")
        sum_tfidf = tfidf_matrix.sum(axis=0)
        sorted_indices = np.argsort(sum_tfidf.A1)[::-1]

        # Get and print the top N terms based on their TF-IDF scores
        top_terms = [feature_names[i] for i in sorted_indices[:n]]

        return top_terms

    #Function to assign themes based on keywords present in the cleaned review
    def assign_themes(self, cleaned_text):
        """
        Assign themes to the cleaned text based on predefined keywords.
        :param cleaned_text: Preprocessed text string.
        :return: List of assigned themes.
        """
        theme_keywords = {
            'Account Access/Login Issues': ['login', 'account', 'access', 'password', 'signin', 'username', 'locked', 'credential', 'verification'],
            'Transaction Issues': ['transfer', 'payment', 'transaction', 'send', 'receive', 'money', 'slow',  'pending', 'fail', 'delay', ],
            'User Interface/Experience (UI/UX)': ['app', 'ui', 'user interface', 'design', 'difficult', 'complex', 'update', 'bug', 'crash',],
            'Customer Support/Service': ['support', 'customer service', 'help', 'contact', 'response', 'reply', 'assist'],
            'Features/Functionality Requests': ['feature', 'add', 'request', 'missing', 'option', 'tool', 'card', 'notification', ]
        }
        # Initialize an empty list to hold assigned themes
        assigned_themes = []
        
        # Iterate through each theme and its keywords
        for theme, keywords in theme_keywords.items():
            # Check if any of the theme's keywords are in the cleaned review
            if any(keyword in cleaned_text for keyword in keywords):
                assigned_themes.append(theme)
        # If no specific themes are assigned, assign a default 'General' theme (optional)
        if not assigned_themes:
            assigned_themes.append('General')
        return assigned_themes