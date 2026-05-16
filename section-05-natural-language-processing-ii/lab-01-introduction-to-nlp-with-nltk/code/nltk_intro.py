import nltk

# Download required datasets
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

# Sample text
text = "Hello! This is an example sentence. Natural Language Processing is fun."

# Sentence Tokenization
sentences = nltk.sent_tokenize(text)
print("\nSentences:")
print(sentences)

# Word Tokenization
words = nltk.word_tokenize(text)
print("\nWords:")
print(words)

# POS Tagging
tagged_words = nltk.pos_tag(words)

print("\nPOS Tagged Words:")
print(tagged_words)
