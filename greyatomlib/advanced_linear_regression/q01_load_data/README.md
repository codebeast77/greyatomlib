## Task 1: Load the data and split it into test and train data set 

Hello budding Data scientist , of all the process we have done of loading and 
splitting of data separately .
Why not do it in single step.  
Your job is to return test and train data set with split ratio of 33 percent.

**The function should**
- Be named as `load_data` .
- Should return a test and training data sets 

#### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | string | compulsory |  | path to the file csv |
| test_size | float | optional | | test split |

#### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| df | Dataframe for Data; CSV acceptable by sklearn | X_train |
| X_train | Dataframe for training, testing; CSV acceptable by sklearn | X_train |
| X_test | Dataframe for training, testing; CSV acceptable by sklearn | X_test |
| y_train | Dataframe for training, testing; CSV acceptable by sklearn | y_train |
| y_test | Dataframe for training, testing; CSV acceptable by sklearn | y_test |