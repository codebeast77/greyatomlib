## Cross validate your model.

Splendidly done,

To the problem of overfitting there are several ways to overcome , one such way is cross validation.
Your job is to apply the method of cross validation and hence record the change in accuracy of model.

This assignment will provide you a good hold on concept such as cross validation when and where to apply this 
concept.

 
**The function should**
- Be named `cross_validation` .
- Should return mean error scores for different cross validation folds.

#### Parameters:

| Parameter | dtype | argument type | default value | description |
| :---: | :---: | :---: | :---: | :---: |
| Model | | compulsory |  | Model to be fitted |
| X | Dataframe for training, testing; any format acceptable by sklearn| compulsory |  | X_test |
| y | Dataframe for training, testing; any format acceptable by sklearn | compulsory |  | y_train |



#### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| mean error scores | | mean of neg_mean_squared_errors for different cross validation folds |
