## Create a Ridge regressor model and measure the accuracy of your linear model.

So far so good,
Feeling expert on building polynomial basis functions huh...

Now ,as you know implementing polynomial basis function increases model complexity and the problem of overfitting arises.

Your job is to improvise L2 (Ridge)  Regularization on linear model created previously. 

Doing this assignment would provide you how to create and apply Ridge regressor method of 
regularization in action.

**The function should**
- Be named `ridge` .
- Should return a model with implementation of L2 (Ridge)  Regularization.
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
