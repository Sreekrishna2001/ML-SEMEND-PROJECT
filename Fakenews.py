import pandas as pd
import numpy as np
data=pd.read_csv('news.csv')
data.isnull().sum()
x=data['title']+' '+data['text']
y=data['label']
# print(x)
# print(y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=0)

from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
model=make_pipeline(TfidfVectorizer(),MultinomialNB())
model.fit(x_train,y_train)


ypred=model.predict(x_test)

# print(ypred)

from sklearn import metrics 
ac=metrics.accuracy_score(y_test,ypred)
# print(ac)


cm=metrics.confusion_matrix(y_test,ypred)

# print(cm)


def prednews(newstitle):
    return(model.predict([newstitle]))

# while True:
#     try:
#         prednews(input())
#     except: break
