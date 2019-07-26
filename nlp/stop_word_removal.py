import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

paragraph = "Hello Guys! It is a pleasure to see you all after such a long time..."

sentences = nltk.sent_tokenize(paragraph)

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences)
    new_words =  [ word for word in words if word not in stopwords.words('English')]
    sentences[i] = ' '.join(new_words)
    