from sklearn.datasets import load_iris
iris = load_iris()
print (iris.feature_names)
print (iris.target_names)
print (iris.data[0])
print (iris.target[0])
for i in range(len(iris.target)):
    print ("Example:"+ str(i) + ", label:" + str(iris.target[i]) + ", features" + str(iris.data[i]))
