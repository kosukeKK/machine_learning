import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
iris     = load_iris()
INDEX = [0, 50, 100] #0,50,100番目でラベルの名前が変わってるからこれにしてる

# iris.target #ラベル
# iris.data   #データ

#training data
target = np.delete(iris.target, INDEX)      #sampleとして抜き取るから元データからラベルを捨てとく
data   = np.delete(iris.data, INDEX, axis=0)#sampleとして抜き取るから元データからデータを捨てとく

sample_target  = iris.target[INDEX]     #インデックスからラベルを取得してる
sample_data    = iris.data[INDEX]       #インデックスからデータを取得してる

clf = tree.DecisionTreeClassifier()
clf.fit(data, target)                   #データとラベルの結びつけ
print (sample_target)
print (clf.predict(sample_data))        #特徴から条件が似てるやつを探し出す
