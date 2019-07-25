import nltk
from nltk.stem import WordNetLemmatizer

paragraph = "Hello Guys! It is a pleasure to see you all after such a long time..."

sentences = nltk.sent_tokenize(paragraph)
lemmetizer = WordNetLemmatizer()

#Lemmetisation process

for  i in range(len(sentences)):
    word = nltk.word_tokenize(sentences[i])
    new_words = [ lemmetizer.lemmatize(word) for word in words]
    sentences = ' '.join(new_words)