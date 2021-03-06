from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange

def svm_loss_naive(W, X, y, reg):
    """
    Structured SVM loss function, naive implementation (with loops).

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    dW = np.zeros(W.shape) # initialize the gradient as zero

    # compute the loss and the gradient
    num_classes = W.shape[1]
    num_train = X.shape[0]
    loss = 0.0
    for i in range(num_train):
        scores = X[i].dot(W)
        correct_class_score = scores[y[i]]
        for j in range(num_classes):
            if j == y[i]:
                continue
            margin = scores[j] - correct_class_score + 1 # note delta = 1
            #print(margin)
            if margin > 0:
                loss += margin
                #Derivative w.r.t w(j) & w(y)
                dW[:, y[i]] -= X[i, :]
                dW[:, j] += X[i, :]
                #print(dW[j])
                #print(grad_w)
            '''
            else:
                grad_w = reg * W[:,j]
            
            dW[:,j] = dW[:,j] + grad_w
            '''    
    # Right now the loss is a sum over all training examples, but we want it
    # to be an average instead so we divide by num_train.
    loss /= num_train
    

    # Add regularization to the loss.
    loss += reg * np.sum(W * W)
    

    #############################################################################
    # TODO:                                                                     #
    # Compute the gradient of the loss function and store it dW.                #
    # Rather than first computing the loss and then computing the derivative,   #
    # it may be simpler to compute the derivative at the same time that the     #
    # loss is being computed. As a result you may need to modify some of the    #
    # code above to compute the gradient.                                       #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    #average teh updates
    dW /= num_train
    #derivative of regulatization parameter
    dW += 2 * reg * W
    #pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    return loss, dW



def svm_loss_vectorized(W, X, y, reg,delta=1.0):
    """
    Structured SVM loss function, vectorized implementation.

    Inputs and outputs are the same as svm_loss_naive.
    """
    loss = 0.0
    dW = np.zeros(W.shape) # initialize the gradient as zero
    num_train = X.shape[0]

    #############################################################################
    # TODO:                                                                     #
    # Implement a vectorized version of the structured SVM loss, storing the    #
    # result in loss.                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    scores = np.dot(X, W)
    correct_class_scores = np.choose(y, scores.T).reshape(-1, 1)

    margins = np.maximum(scores - correct_class_scores + delta, 0.0)
    # We currently have num_train * delta error in our matrix, since we should
    # not add delta to the correct class indices. For all i=[0..num_train],
    # j=y[i] set margins[i,j] = 0.0.
    margins[np.arange(num_train), y] = 0.0

    # Right now the loss is a matrix of all training examples. We want it to be
    # scalar average instead, so we sum and we divide by num_train.
    loss = np.sum(margins) / float(num_train)

    # Add L2 regularization to the loss.
    loss += reg * np.sum(W * W)

    #pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    #############################################################################
    # TODO:                                                                     #
    # Implement a vectorized version of the gradient for the structured SVM     #
    # loss, storing the result in dW.                                           #
    #                                                                           #
    # Hint: Instead of computing the gradient from scratch, it may be easier    #
    # to reuse some of the intermediate values that you used to compute the     #
    # loss.                                                                     #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    #pass
    grad_mask = (margins > 0).astype(int)
    grad_mask[np.arange(y.shape[0]), y] = - np.sum(grad_mask, axis=1)
    dW = np.dot(X.T, grad_mask)

    dW /= float(num_train)
    dW += 2 * reg * W

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
