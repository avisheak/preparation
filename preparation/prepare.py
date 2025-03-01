import re
import pandas as pd

def tokenize_sentences_bengali(text):
    pattern = r'।|\?|!'  # Common sentence delimiters in Bengali
    sentences = re.split(pattern, text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return sentences
    
def tokenize_words_bengali(sentence):
    return sentence.split()

stopwords_url = 'https://raw.githubusercontent.com/avisheak/preparation/main/stopwords_bangla.csv'
stopwords_df = pd.read_csv(stopwords_url)
stopwords = set(stopwords_df['words'].tolist())

def remove_stopwords(tokens):
    return [token for token in tokens if token not in stopwords]

def merge_lists(list1, list2):
    # Use the or operator to fall back to an empty list if the list is None
    list1 = list1 or []
    list2 = list2 or []
    return list1 + list2 # Concatenate both lists

def unwanted_text_remove(text, list):
    if not isinstance(text, str):
        return text  # Return as is if not a string
    
    unwanted_substrings = ["আরো পড়ুন", "বিস্তারিত", "আরো জানুন"]
    unwanted_substrings = merge_lists(unwanted_substrings, list)
    
    for substring in unwanted_substrings:
        text = text.replace(substring, "")
    
    # Return the cleaned text, stripped of leading/trailing spaces
    return text.strip()
    
def custom_stemmer(word):
    suffixes = ['ের', 'কে', 'দের', 'র', 'তে', 'ও', 'ওয়া']  # Add more suffixes as needed
    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

def stem_words(tokens):
    return [custom_stemmer(word) for word in tokens]

def prepare(
    text, 
    list=None):
    text = unwanted_text_remove(text, list)
    sentences = tokenize_sentences_bengali(text)
    tokenized_sentences = [tokenize_words_bengali(sentence) for sentence in sentences]
    cleaned_sentences = [remove_stopwords(tokens) for tokens in tokenized_sentences]
    stemmed_sentences = [stem_words(tokens) for tokens in cleaned_sentences]
    sentence = " ".join(stemmed_sentences[0])
    sentence
    return sentence
