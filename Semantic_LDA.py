import codecs
import glob
import re

import enchant
import gensim
from gensim import corpora
from nltk.corpus import stopwords


dict = enchant.Dict("en_US")

filepath = "/home/bigdata/PycharmProjects/PyLDA/Hackathon/data/now.txt"
s = []
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
all_documents = glob.glob(filepath)

from nltk.tokenize import word_tokenize

for v in all_documents:
    x = codecs.open(v, "r", encoding='utf-8', errors='ignore').read()
    v = word_tokenize(x)
    lem = [lemmatizer.lemmatize(t.lower()) for t in v]
    s.append(lem)

from nltk.stem import WordNetLemmatizer

wnl = WordNetLemmatizer
stoplist = set(
    open("/home/bigdata/PycharmProjects/PyLDA/KLDivergence/data/stopwords.txt").read().split('\n'))

texts = [[word for word in list_sentences if len(word) > 3 if word not in stoplist if
          word not in stopwords.words('english') and dict.check(word) and re.search('[a-zA-Z]', word)]
         for list_sentences in s]

# Creating the term dictionary of our courpus, where every unique term is assigned an index. dictionary = corpora.Dictionary(doc_clean)
dictionary = corpora.Dictionary(texts)
# dictionary.save('pubmed.dict')
dictionary.save('pubmed.dict')
print(dictionary)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in texts]
corpora.MmCorpus.serialize('pubmed.mm', doc_term_matrix)

print('length of document term matrix')
print(len(doc_term_matrix))
# print(doc_term_matrix[100])

# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=10, id2word=dictionary, passes=50)
print(ldamodel.print_topics(num_topics=2, num_words=4))

for i in ldamodel.print_topics():
    for j in i: print(j)

ldamodel.save('pubmed.model')
from gensim.models import LdaModel

loading = LdaModel.load('pubmed.model')

print(loading.print_topics(num_topics=2, num_words=4))
