# MNIST_KNN
This module is limited to making use of the classifier KNeighborsClassifier from sklearn to apply it to the recognition of handwritten digits in the MNIST file, with a hit rate higher than 95% and extraordinary simplicity, especially compared to the complexity of classifiers based on neural networks. It also shows full sensitivity.

Functioning:

It is required that on disk C: you will find the files:
mnist_train.csv
mnist_test.csv
downloaded from
https://www.kaggle.com/oddrationale/mnist-in-csv

The program is run from Spyder:
MNIST_KNN_sklearn_with_test_out_train.py

The program is adapted to follow-up one by one of the test images, instead of a global calculation of the hit rate.
It can give problems of lack of memory in low-performance computers, despite the fact that the margin of test files records is reduced from 1 to 100. By changing the value of ContaMax to 10000 in line 10, the 10000 records of the test file mnist_test.csv would be processed, in case you have a computer and a python version that overcomes the out of memory problems.

Sensitivity tests have been done by processing the mnist_test20.csv file, it is enough to change the file assignment of line 11, which gives 20 hits and 0 failures and then processed the mnist_test20_bad.csv, which is the mnist_test20.csv with the classes of the last three registers changed, verifying that 17 hits and 3 failures appear, that is, errors entered are detected. both files are accompanied.

Comparing acuracy with others models from sklearn:

https://github.com/ablanco1950/ABALONE_DECISIONTREE_C4-5/blob/main/GBT2.ipynb

References:

https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html

https://www.kaggle.com/oddrationale/mnist-in-csv

Projects on MNIST that make use of the classifier based on neural networks:

https://github.com/louisjc/mnist-neural-network/blob/master/neural_net.py

https://github.com/kdexd/digit-classifier
