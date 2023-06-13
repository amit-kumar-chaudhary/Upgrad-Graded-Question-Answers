#!/usr/bin/env python
# coding: utf-8

# **Q1 - Random Forest**
# 
# Which of the following information is NOT true with respect to Random Forest?
# 
# 1. In a random forest, all of the trees are independent to each other.
# 
# 2. Random selection of an equal number of data points is used for training each of the trees.
# 
# 3. Random selection of an equal number of features used in building each of the trees.
# 
# 4. **The training process of individual trees in a random forest is the same as training a decision tree.**
#     - This is not true. Training process of each tree in a Random forest is same as a decision tree except with the difference that at each node in the tree only a random selection of features is used for the split in that node.

# **Q2 - Random Forests over Decision Trees**
# 
# Which of the following is/are benefit(s) of random forest over a decision tree? (More than one option may be correct.)
# 
# 
# 1. **It is more stable than a decision tree**
# 
# 2. **It reduces overfitting**
# 
# 3. Interpretability increases after using Random Forest
# 
# 4. **It is immune to the curse of dimensionality**

# **Q3 - Decision Trees**
# 
# Consider decision tree A learned with min_samples_leaf = 500. Now consider decision tree B trained on the same dataset and parameters, except that the min_samples_leaf=50. Which of the following is/are always true? (More than one option may be correct.)
# 
# 
# 1. **The depth of B >= the depth of A**
# 
#     - min_samples_leaf guarantees a minimum number of samples in a leaf. Higher no of this parameter means you are stopping early. A lower value allows you to grow further.
# 
# 
# 2. **The number of nodes in B >= the number of nodes in A**
#     
#     - min_samples_leaf guarantees a minimum number of samples in a leaf. Higher no of this parameter means you are stopping early. A lower value allows you to grow further. As the tree grows no of nodes increases.
# 
# 
# 3. The test error of B <= the test error of A
# 
# 
# 4. **The training error of B <= the training error of A**
# 
#     - min_samples_leaf guarantees a minimum number of samples in a leaf. Higher no of this parameter means you are stopping early. A lower value allows you to grow further. As the tree grows no of nodes increases. With more nodes and deeper tree , it tends to memorize training data and variance of the model increases.

# **Q4 - OOB Error**
# 
# Select all that apply with regards to OOB or Out of Bag Error. (More than one option may be correct)
# 
# 
# 1. **All the data points in the training set are considered while calculating the OOB error.**
# 
#     - Correct! All the observations of the training set are used to calculate the OOB error.
# 
# 
# 2. All the data points in the training and test sets are considered while calculating the OOB error.
# 
# 
# 3. Each data point in the training set is considered for all the trees in the random forest while calculating the OOB error.
# 
# 
# 4. **Each data point in the training set is considered only for some of the trees in the random forest while calculating OOB error.**
# 
#     - Correct. Each data point is considered to calculate OOB error, but for each of the points, only the trees which didn't have that data point in their bootstrap sample will be considered to calculate the OOB error.
# 
# 

# **Q5 - Feature Importance in Random Forests**
# 
# How do you calculate feature importance in random forests for a particular attribute?
# 
# 
# 1. We select the best-performing tree in the random forest and calculate the feature importance from that tree.
# 
# 
# 2. We take an attribute and check all the trees it was present in and then check in which of the trees the change in the homogeneity on this attribute split is the highest. This highest value of change in the homogeneity gives us the feature importance of that attribute.
# 
# 
# 3. **We take an attribute and check all the trees it was present in and take the average values of the change in the homogeneity on this attribute split. This average value of change in the homogeneity gives us the feature importance of that attribute.**
# 
#     - Recall that we take all the trees that attribute was present in and aggregate the homogeneity measures to calculate feature importance. We basically select all the trees the attribute was present in and calculate the ΔHomogeneity on the attribute split. We then take an average of all of these ΔHomogeneity to arrive at the final feature importance.
# 
# 
# 4. The total number of trees the attribute was present in divided by the total number of trees gives us the feature importance of that attribute.
