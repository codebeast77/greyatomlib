##  To create a  unique polynomial basis function combining top correlated varibles.

Nice work ,keep that spirit.
As we have seen in our lectures we have known what is polynomial basis function and what is it used for.

Your job is create a polynomial basis function using the top four correlated variables.

**The function should**
- Be named `polynomial` .
- Should return a model with implementation of polynomial basis function.
- All the process should be done with random state set as 9 and power parameter should be set as 5.
- Should be able to load the data with the help of function `load_data`.
- Should be able to extract 'OverallQual','GrLivArea','GarageCars','GarageArea' features
  and fit model on these features.
 
Doing this assignment will help you learn how to create polynomial basis function and fit it onto linear model.
You can also toy with the parameters and observe the effect on your linear model.

#### Parameters:


| Parameter | dtype | argument type | default value | description |
| :---: | :---: | :---: | :---: | :---: |
| X_train | Dataframe for training, testing; any format acceptable by sklearn| compulsory |  | X_train |
| X_test | Dataframe for training, testing; any format acceptable by sklearn| compulsory |  | X_test |
| power | Numeric Number | optional | 4 | power |

#### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| Model |  | Model for polynomial linear regression |

Excited! The let's get started. 