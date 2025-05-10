import nltk
import pandas as pd
import string
from sklearn.feature_extraction. text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

nltk.download('stopwords')
nltk.download('punkt')
desired_width = 400
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 20)
stopwords_set = set (nltk.corpus.stopwords.words ('english'))
punctuation_set = set(string.punctuation)
print('# stopwords =', len(stopwords_set),'  # punctuations =', len(punctuation_set))
print(' ')
data_file = 'Procedure3.txt' # assigns var data_file
df = pd.read_table (data_file, header=None)
df.columns= ('surgicalArea', 'procedure')
df['proc_cleaned'] =df.procedure.apply(lambda x: ' '.join([word for word in x.split() if word not in stopwords_set and word not
                    in punctuation_set]))
df['proc_cleaned'] = df.proc_cleaned.str.lower()
print(df.head(4))
print(' ')

TFIDF_vector = TfidfVectorizer()
TFIDF_vector1 = TfidfVectorizer (ngram_range=(1,3))
X = TFIDF_vector.fit_transform (df.proc_cleaned)
X1 = TFIDF_vector1.fit_transform(df.proc_cleaned)
print('TFIDF vector X matrix type = ', type (X), 'X matrix shape = ', X. shape)
print('TFIDF* vector X1 matrix type', type (X1), 'X1 matrix shape = ', X1. shape)

y= df.surgicalArea
X_train, X_test, y_train, y_test = train_test_split(X,y)
X1_train, X1_test, y1_train, y1_test = train_test_split(X1,y)
print(' ')

Logreg = LogisticRegression (max_iter=1000)
Logreg1 = LogisticRegression (max_iter=1000)
Logreg2 = LogisticRegression (max_iter=1000)

Logreg.fit(X_train,y_train)
Logreg1.fit(X1_train,y1_train)


y_pred = Logreg.predict(X_test)
y1_pred = Logreg1.predict(X1_test)
LogregXR2 = Logreg.score (X_test,y_test)
LogregX1R2 = Logreg1.score (X1_test,y1_test)
print('Logistic Regression X R2 ',LogregXR2)
print('Logistic Regression X1 R2', LogregX1R2)
type_err_matrix = confusion_matrix(y_test, y_pred)
type_err_matrix1 = confusion_matrix(y1_test,y1_pred)
print(type_err_matrix, 'Confusion Matrix [y_test, y_pred]')
print(type_err_matrix1,'Confusion Matrix [y1_test, y1_pred]')

rf = RandomForestClassifier()
rf1 = RandomForestClassifier()
rf2 = RandomForestClassifier()

rf.fit(X_train,y_train)
rf1.fit(X1_train,y1_train)
y2_pred = rf.predict(X_test)
y3_pred = rf1.predict(X1_test)
print('rfscore', rf.score(X_test,y_test))
print('r1fscore', rf1.score(X1_test,y1_test))

type_err_matrix3 = confusion_matrix(y_test,y2_pred)                              # calculate Type I & II errors - X,y
type_err_matrix4 = confusion_matrix(y1_test,y3_pred)                             # calculate Type I & II errors - X1,y1
print(type_err_matrix3, ' <--------------- Confusion Matrix [y_test,y2_pred]')    # display Type I & II errors - X,y
print(type_err_matrix4, ' <--------------- Confusion Matrix [y1_test,y3_pred]')   # display Type I & II errors - X1,y1

print('Logistic reg. w/ TFIDF',confusion_matrix(y_test,y_pred))
print('Random forest w/ TFIDF',confusion_matrix(y_test,y2_pred))
print('Logistic reg. w/ TFIDF',confusion_matrix(y1_test,y1_pred))
print('Random forest w/ TFIDF',confusion_matrix(y1_test,y3_pred))

