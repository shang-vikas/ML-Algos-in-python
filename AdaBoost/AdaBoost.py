import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split
from sklearn.datasets import make_hastie_10_2
import matplotlib.pyplot as plt


class Dataset(object):
    
    def __init__(self,X,Y):
        if not isinstance(X,np.ndarray):
            X = np.array(X,copy=False)
        
        if not isinstance(Y,np.ndarray):
            Y = np.array(Y,copy=False)

    def get(self):
        return X,Y

class TreeNode:
    
    def __init__(self):
        self.is_leaf = False
        self.left_child = None
        self.right_child = None
        self.split_feature_id = None
        self.split_gain = 0.
        self.epsilon = 0.0001
    
    def _calc_entropy(instances,features):
        freq_ = np.unique(instances,return_counts=True)[1]
        proba = freq_/freq_.sum()
        entropy = (-1*proba*np.log2(proba)).sum()
    
    
    def build(self,X,Y,param,depth,shrinkage):
        
    
    def predict(self):
        pass
        
class Tree:
    
    def __init__(self):
        self.root = None
        
        
    def build(self,train_set,params,depth,shrinkage):
        pass
    
    def predict(self,train_set):
        pass
    
class AdaBooster(object):
    def __init__(self,n_estimators,criterion='gini',learning_rate=0.1,sample_weight=None,max_depth=None):
        '''
        Adaboost Implementation from schapire paper
        max_depth = None(default=3)
        criterion = ['gini','entropy']-->default='gini'
        
        ## Gini = 1 - np.square(p).sum()
        ## entropy = -(p*np.log(p)).sum()
        ## information Gain,## Gain Ratio
        
        '''
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.sample_weight = sample_weight
        self.max_depth = max_depth
        self.estimators = []
        self.estimators_errors = []
        self.estimators_beta = []
        
        if self.max_depth is None:
            self.max_depth = 3
        
    def _build_learner(self,train_set,max_depth):
        self.root = Tree()
        self.root.build()
        return self.root
    
    def fit(self,X,Y):
        
        self.X,self.Y = Dataset(X,Y).get()
        
        if self.sample_weight is None:
            self.sample_weight = np.ones(len(Y))/len(Y)
        
        for cnt in range(n_estimators):
            estimator = self._build_learner(self.X,self.Y,sample_weight,learning_rate,max_depth)
            self.estimators.append(estimator)
            error = estimator.get_error(self.X,self.Y)
            
    
    def predict(self,X):
        scores = np.array([sum([m.predict(X[idxx]) for m in self.estimators]) for idxx in range(len(X))])
        
    
    
    