### Summary
The repo contains solutions for the [CS231n](https://github.com/pandao/editor.md "Heading link") Stanford Course

#### Assignment 1
                

+ Q1: k-Nearest Neighbor Classifier - KNN algorithm implementation
    + [knn.ipynb](https://github.com/jim-j-james/cs231n/blob/main/assignment1/knn.ipynb)
		+ Utilises the CIFAR10 dataset with 5000 training and 500 test records.
		+ Computes the distance metric with two, one and no loops. <np.newxis>
		+ Crossvalidates with different values of K to find the optimal one.
    + [k_nearest_neighbor.py](https://github.com/jim-j-james/cs231n/blob/main/assignment1/cs231n/classifiers/k_nearest_neighbor.py)
		+ Implemetation of distance metric with two, one and no loops.
		+ Implements the Knn logic where the  most frequent out of k neighbors are assigned to each point

+ Q2: Training a Support Vector Machine - SVM Implementation
    + [svm.ipynb](https://github.com/jim-j-james/cs231n/blob/main/assignment1/svm.ipynb)
		+ Utilises the CIFAR10 dataset with 49000 training and 1000 test records. 500 dev and 1000 test records are considered for code build as well.
		+ Preprocess the image my subtracting the mean image and adding the bias column to the weights.
		+ Compute the loss and derivative through linear_svm.py/svm_loss_naive function through mutliple loops  
    + [linear_svm.py](https://github.com/jim-j-james/cs231n/blob/main/assignment1/cs231n/classifiers/linear_svm.py)
		+ svm_loss_naive
			+ Compute the margin score for each record aganist the incorrect classes and accumalate the loss. Average the loss and add regulaisation
			+ Accumalate the derivative, average it and add regularisation
			+ Return the cumilative loss and derivative
