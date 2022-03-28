from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

input_str="NLTK is a leading platform for building Python programs to work with human language data."

stop_words=set(stopwords.words('english'))

tokens=word_tokenize(input_str)

result=[i for i in tokens if not i in stop_words]
print(result) 












