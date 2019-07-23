import nltk
from nltk.stem import PorterStemmer

paragraph = "Hello Guys! It is a pleasure to see you all after such a long time..."
sentences  = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    new_words = [ stemmer.stem(word) for word in words]
    sentences[i] = ' '.join(new_words)

print(sentences)
print(words)
