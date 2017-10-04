## Create a Lasso regressor model and measure the accuracy of your linear model.

Your job is to improvise L2 (Ridge)  Regularization on linear model created previously. 


This assignment will help you how to create and apply Lasso regressor method of 
regularization in action and also provide a way to implement feature selection which comes handy 
often times.
 
**The function should**
- Be named `lasso` .
- Should return a model with implementation of L1 (Lasso)  Regularization.
- RMSE for train data set.
- RMSE for test data set.
- Should be able to load the data with the help of function `load_data`.

Note : The random seed and as well as random state should be set as 9. 

#### Parameters:


| Parameter | dtype | argument type | default value | description |
| :---: | :---: | :---: | :---: | :---: |
| X_train | Dataframe for training, testing; any format acceptable by sklearn| compulsory |  | X_train |
| X_test | Dataframe for training, testing; any format acceptable by sklearn| compulsory |  | X_test |
| y_train | Dataframe for training, testing; any format acceptable by sklearn | compulsory |  | y_train |
| Y_test | Dataframe for training, testing; any format acceptable by sklearn| compulsory |  | Y_test |
| alpha | Numeric Number | optional | 1 | learning_rate |

#### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| RMSE for train | float | Rmse for Ridge regressor |
| RMSE for test | float | Rmse for Ridge regressor |
| Model |  | Model for Ridge linear regression |
