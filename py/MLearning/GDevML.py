from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
Y = iris.target

from sklearn.cross_validation import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.5)

myclf = KNeighborsClassifier()
myclf.fit(X_train, Y_train)

predition = myclf.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test, predition))