# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 17:54:27 2019

@author: amukher3
"""

import pandas as pd
import xgboost as xgb
import numpy as np
from numpy import sort
from xgboost import XGBClassifier
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/amukher3/Downloads/DScasestudy.txt",sep='\t')
X = df.iloc[:, 1:].values
y = df['response']

#Checking for class imbalance
y.value_counts()

# fitting the model for all the features 
model = XGBClassifier()
model.fit(X, y)


# A pictorial representation of the feature importances 
# based on the F-score.
fig, ax = plt.subplots(figsize=(12,18))
xgb.plot_importance(model, max_num_features=50, height=0.8, ax=ax)
plt.show()

sorted_idx = np.argsort(model.feature_importances_)[::-1]


# Using CV to find the best model

# Fit model with different features based on the importance 
# For each combination use n-fold CV to get the AUC 

thresholds = sort(model.feature_importances_)
thresholds=thresholds[-30:]

for thresh in thresholds:
    
# select features using threshold
    selection = SelectFromModel(model, threshold=thresh, prefit=True)
    select_X= selection.transform(X)
    xgtrain = xgb.DMatrix(select_X, label=y)
    
    clf = xgb.XGBClassifier()
    xgb_param = clf.get_xgb_params()
    #do cross validation
    print ('Start cross validation')
    cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=5000, nfold=5, metrics=['auc'],
                      early_stopping_rounds=50, stratified=True, seed=1301)
    print('Best number of trees = {}'.format(cvresult.shape[0]))
    clf.set_params(n_estimators=cvresult.shape[0])
    print('Fit on the trainingsdata')
    clf.fit(select_X, y, eval_metric='auc')
    print("Thresh=%.3f, n=%d" % (thresh, select_X.shape[1]) )   
    print('Overall AUC:', roc_auc_score(y, clf.predict_proba(select_X)[:,1]))
    

############################# Selecting the best model #######################
   
####################### The best features ##########################
    
# Above we used CV to see the effect of features with different importances.
# We found that the threshold corresponding to the 30 th index i.e n=30 gives the
# best CV-AUC of 0.96. 
# n=30 corresponds to a threshold value of 0.007 i.e all features above that
# threshold are included in the final model.
# The final model(FinalModel) is developed using these features and shoudl be 
# for testing with the test data.  
    
#Thrshold = 0.007 for n=30   

n_cutoff=30    
threshold=thresholds[n_cutoff-1]  

selection_new = SelectFromModel(model, threshold, prefit=True)
FinalFeatureList= selection_new.transform(X)

#Final Model
Finalmodel = XGBClassifier()
  
# The next few lines splits the data into train-test the test size being 20%
# of the original data size and reports the AUC on the test set. 
# The test AUC is around 0.89. 

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(FinalFeatureList, y, test_size=0.2, random_state=100) 


# Fitting the model to the features selected.
Finalmodel.fit(X_train, y_train) 

y_pred = Finalmodel.predict(X_test)
predictions = [round(value) for value in y_pred]

from sklearn.metrics import accuracy_score

# evaluate predictions 
accuracy = accuracy_score(y_test, predictions)
print("Test set accuracy is: %.2f%%" % (accuracy * 100.0))


    
   
   