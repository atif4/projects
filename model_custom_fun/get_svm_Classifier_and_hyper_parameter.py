"""use the GridSearchCV module in order to test a number of combinations of parameters 
that can optimize the performance of our model.For hyperparameter tuning we have 3 parameters to consider:

Kernel=rbf (radial basis function): kernel functions are used to map the original dataset (linear/nonlinear ) 
into a higher dimensional space with a view to making it a linear dataset.

C parameter: It is a hypermeter in SVM to control error. It acts as a penalty parameter, a small value of C will result
in a larger margin separating the hyperplane. If we don’t want our training points to be misclassified, then we go for a
large value of C, which will result in a smaller margin separating plane, but it can lead to an overfitting problem where 
the model may not generalize well on training data.

Gamma parameter: This will decide the curvature of the decision boundary, higher the gamma, the greater is the curvature of
the decision boundary."""
def get_svm_Classifier_and_hyper_parameter():
    #Create a svm_Classifier and hyper_parameter tuning 
    ml = svm.SVC() 
  
    # defining parameter range
    param_grid = {'C': [ 1, 10, 100, 1000,10000],'gamma': [1,0.1,0.01,0.001,0.0001],'kernel': ['rbf']} 
  
    grid = GridSearchCV(ml, param_grid, refit = True, verbose = 1,cv=15)
  
    # fitting the model for grid search
    grid_search = grid.fit(X_train, y_train)