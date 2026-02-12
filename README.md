UPI stands for Unified Payment Interface that is an instant Indian Payment system.

4 models have been used Decision Tree, Random Forest, XGBoost , GradientBoost.
Out of which XGBoost is the one that is performing the best so after data balancing by SMOTE (a type of oversampling technique) and then i did Model Optimization by HyperParameter Tuning via GridSearchCV (However 
RandomisedSearch CV is preferred over it due to effieciency reasons but still i used gridsearch CV) and then after knowing the optimal hyperparameters i used XGboost along with those Hyperparameters .

Achieved accuracy is 93.75%.
